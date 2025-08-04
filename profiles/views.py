from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .forms import UserProfileForm
from .models import UserProfile
from checkout.models import Order
import json

@login_required
def profile(request):
    """ Display the user's profile. """
    # Get the user's profile or return 404 if not found
    profile = get_object_or_404(UserProfile, user=request.user)
    
    # Force refresh from database to get latest data
    profile.refresh_from_db()

    if request.method == 'POST':
        # Check if this is a notification preferences submission
        if 'default_email_notifications' in request.POST:
            # Handle notification preferences form
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                # Save only the notification preference fields
                profile.default_email_notifications = form.cleaned_data['default_email_notifications']
                profile.default_order_status_updates = form.cleaned_data['default_order_status_updates']
                profile.default_promotional_emails = form.cleaned_data['default_promotional_emails']
                profile.default_newsletter_subscription = form.cleaned_data['default_newsletter_subscription']
                profile.save()
                messages.success(request, 'Notification preferences updated successfully!')
            else:
                messages.error(request, 'Failed to update notification preferences. Please try again.')
        else:
            # Handle main profile form
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                # Save the updated profile if the form is valid
                form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                # Show error message if the form is invalid
                messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        # If not a POST request, instantiate the form with the current profile
        form = UserProfileForm(instance=profile)
    
    # Get all orders related to the user's profile, ordered by date descending
    # Limit to last 10 orders to prevent dashboard clutter
    orders = profile.orders.all().order_by('-date')[:10]
    
    # Get cart item count for the orders section
    from cart.contexts import cart_contents
    cart = cart_contents(request)
    product_count = cart['product_count']

    template = 'profiles/dashboard.html'
    context = {
        'form': form,
        'orders': orders,
        'product_count': product_count,
        'user_preferences': profile,  # Pass profile as user_preferences for template
        'on_profile_page': True
    }

    # Render the profile dashboard template with the context
    return render(request, template, context)

@login_required
def order_history(request, order_number):
    """
    Display a user's past order confirmation.
    """
    # Get the order by order_number or return 404 if not found
    order = get_object_or_404(Order, order_number=order_number)

    # Inform the user that this is a past order confirmation
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'profiles/order_history.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    # Render the order history template with the context
    return render(request, template, context)

def login_view(request):
    """
    Handle user login with enhanced validation
    """
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        email = request.POST.get('login', '').strip()
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me') == 'on'  # Check if remember me is checked
        
        # Enhanced validation
        errors = {}
        
        # Email validation
        if not email:
            errors['email'] = 'Email is required'
        elif not '@' in email or not '.' in email:
            errors['email'] = 'Please enter a valid email address'
        
        # Password validation
        if not password:
            errors['password'] = 'Password is required'
        
        # If there are validation errors, return them
        if errors:
            for field, error in errors.items():
                messages.error(request, f'{field.title()}: {error}')
            return render(request, 'registration/login.html', {'errors': errors})
        
        # Try to get user by email
        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password. Please check your credentials and try again.')
            return render(request, 'registration/login.html')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Merge persistent cart with session cart if user had items as guest
            persistent_cart = request.COOKIES.get('persistent_cart', '{}')
            try:
                persistent_cart_data = json.loads(persistent_cart)
                if persistent_cart_data:
                    # Get current session cart
                    session_cart = request.session.get('cart', {})
                    # Merge carts (session cart takes precedence for conflicts)
                    merged_cart = {**persistent_cart_data, **session_cart}
                    request.session['cart'] = merged_cart
                    # Clear the persistent cart cookie since it's now in session
                    response = redirect(request.GET.get('next', 'profile'))
                    response.delete_cookie('persistent_cart')
                    
                    # Handle remember me functionality
                    if remember_me:
                        # Set session to expire in 30 days (remember me)
                        request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days in seconds
                        messages.success(request, f'Welcome back, {user.first_name or user.username}! You will stay logged in for 30 days.')
                        response.set_cookie('remembered_email', email, max_age=30 * 24 * 60 * 60)  # 30 days
                    else:
                        # Set session to expire when browser closes (default behavior)
                        request.session.set_expiry(0)
                        messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                        response.delete_cookie('remembered_email')
                    
                    return response
            except (json.JSONDecodeError, TypeError):
                pass  # If persistent cart is invalid, just continue normally
            
            # Handle remember me functionality (if no cart merging was needed)
            if remember_me:
                # Set session to expire in 30 days (remember me)
                request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days in seconds
                messages.success(request, f'Welcome back, {user.first_name or user.username}! You will stay logged in for 30 days.')
                
                # Create response with cookie for remembered email
                response = redirect(request.GET.get('next', 'profile'))
                response.set_cookie('remembered_email', email, max_age=30 * 24 * 60 * 60)  # 30 days
                return response
            else:
                # Set session to expire when browser closes (default behavior)
                request.session.set_expiry(0)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                
                # Remove the remembered email cookie if it exists
                response = redirect(request.GET.get('next', 'profile'))
                response.delete_cookie('remembered_email')
                return response
        else:
            messages.error(request, 'Invalid email or password. Please check your credentials and try again.')
    
    return render(request, 'registration/login.html')

def signup_view(request):
    """
    Handle user registration with enhanced validation
    """
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Enhanced validation
        errors = {}
        
        # Name validation
        if not first_name:
            errors['first_name'] = 'First name is required'
        if not last_name:
            errors['last_name'] = 'Last name is required'
        
        # Email validation
        if not email:
            errors['email'] = 'Email is required'
        elif not '@' in email or not '.' in email:
            errors['email'] = 'Please enter a valid email address'
        elif User.objects.filter(email=email).exists():
            errors['email'] = 'An account with this email already exists'
        
        # Password validation
        if not password1:
            errors['password1'] = 'Password is required'
        elif len(password1) < 8:
            errors['password1'] = 'Password must be at least 8 characters long'
        
        if not password2:
            errors['password2'] = 'Please confirm your password'
        elif password1 != password2:
            errors['password2'] = 'Passwords do not match'
        
        # If there are validation errors, return them
        if errors:
            for field, error in errors.items():
                messages.error(request, f'{field.title()}: {error}')
            return render(request, 'registration/signup.html', {'errors': errors})
        
        try:
            # Create user with email as username
            user = User.objects.create_user(
                username=email,  # Use email as username
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )
            
            # Create user profile
            UserProfile.objects.create(user=user)
            
            # Log the user in
            login(request, user)
            messages.success(request, f'Welcome to CNCraft, {first_name}! Your account has been created successfully.')
            
            return redirect('profile')
            
        except Exception as e:
            messages.error(request, 'An error occurred while creating your account. Please try again.')
            print(f"Signup error: {e}")  # For debugging
    
    return render(request, 'registration/signup.html')

@login_required
def logout_view(request):
    """
    Handle user logout - no template needed, just logout and redirect
    """
    if request.user.is_authenticated:
        user_name = request.user.first_name or request.user.username
        logout(request)
        messages.success(request, f'Goodbye {user_name}! You have been successfully logged out.')
    
    # Clear the remembered email cookie
    response = redirect(request.GET.get('next', 'home'))
    response.delete_cookie('remembered_email')
    return response

def forgot_password_view(request):
    """
    Handle forgot password requests
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        
        try:
            user = User.objects.get(email=email)
            
            # For course project - simulate sending email
            messages.success(request, 
                f'Password reset instructions have been sent to {email}. '
                f'Please check your email inbox.')
            
            # Demo logging 
            print(f"PASSWORD RESET REQUEST for: {email}")
            print(f"User found: {user.first_name} {user.last_name}")
            
            return redirect('account_login')
            
        except User.DoesNotExist:
            # Security: Don't reveal if email doesn't exist
            messages.success(request, 
                f'If an account with {email} exists, reset instructions have been sent.')
            return redirect('account_login')
    
    return render(request, 'registration/password_reset_form.html')  # ← Fixed!

@login_required
def update_user_view(request):
    """
    Handle user account updates (email, password, profile, and billing)
    """
    # Get the user's profile
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        updates_made = False
        
        # Handle email update
        if 'new_email' in request.POST:
            new_email = request.POST.get('new_email')
            confirm_email = request.POST.get('confirm_new_email')
            
            if new_email and confirm_email:
                if new_email == confirm_email:
                    if new_email != request.user.email:
                        # In a real app, you'd validate the email and send confirmation
                        request.user.email = new_email
                        request.user.save()
                        messages.success(request, 'Email address updated successfully!')
                        updates_made = True
                    else:
                        messages.info(request, 'New email is the same as current email.')
                else:
                    messages.error(request, 'Email addresses do not match.')
            else:
                messages.error(request, 'Please fill in both new email fields.')
        
        # Handle phone update (independent, not elif)
        if 'new_phone' in request.POST:
            new_phone = request.POST.get('new_phone')
            confirm_phone = request.POST.get('confirm_new_phone')
            
            if new_phone and confirm_phone:
                if new_phone == confirm_phone:
                    if new_phone != profile.default_phone_number:
                        profile.default_phone_number = new_phone
                        profile.save()
                        
                        # Force refresh from database
                        profile.refresh_from_db()
                        
                        messages.success(request, 'Phone number updated successfully!')
                        updates_made = True
                    else:
                        messages.info(request, 'New phone is the same as current phone.')
                else:
                    messages.error(request, 'Phone numbers do not match.')
            else:
                messages.error(request, 'Please fill in both new phone fields.')
        
        # Handle password change
        if 'new_password1' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                password_form.save()
                messages.success(request, 'Password changed successfully!')
                updates_made = True
            else:
                messages.error(request, 'Password change failed. Please check your input.')
        
        # Handle profile update (shipping address)
        if 'default_street_address1' in request.POST:
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Shipping address updated successfully!')
                updates_made = True
            else:
                messages.error(request, 'Profile update failed. Please check your input.')
        
        # Handle payment details (placeholder for now)
        if 'card_holder_name' in request.POST:
            # For now, just show a success message
            # In a real implementation, you'd save this to a payment model
            messages.success(request, 'Payment details saved successfully!')
            updates_made = True
        
        # Only redirect if updates were made
        if updates_made:
            return redirect('profile')
    
    # Create forms for display
    password_form = PasswordChangeForm(request.user)
    profile_form = UserProfileForm(instance=profile)
    
    context = {
        'password_form': password_form,
        'form': profile_form,  # For profile editing
        'current_email': request.user.email,
    }
    
    return render(request, 'profiles/update_user.html', context)

@login_required
def delete_account_view(request):
    """
    Handle account deletion confirmation
    """
    if request.method == 'POST':
        # User confirmed deletion
        user_name = request.user.first_name or request.user.username
        request.user.delete()  # This will also delete the UserProfile due to CASCADE
        messages.success(request, f'Account for {user_name} has been permanently deleted.')
        return redirect('home')
    
    return render(request, 'profiles/delete_account.html')

@login_required
@require_POST
def delete_order_view(request, order_number):
    """
    Delete a specific order for the authenticated user
    """
    try:
        # Get the order and ensure it belongs to the current user
        order = get_object_or_404(Order, order_number=order_number, user_profile__user=request.user)
        
        # Delete the order
        order.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Order deleted successfully'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)
