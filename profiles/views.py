from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from .forms import UserProfileForm
from .models import UserProfile
from checkout.models import Order

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
    orders = profile.orders.all().order_by('-date')
    
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

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    # Render the checkout success template with the context
    return render(request, template, context)

def login_view(request):
    """
    Handle user login
    """
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        email = request.POST.get('login')
        password = request.POST.get('password')
        
        # Try to get user by email
        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return render(request, 'registration/login.html')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            
            # Redirect to next page or profile
            next_page = request.GET.get('next', 'profile')
            return redirect(next_page)
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'registration/login.html')

def signup_view(request):
    """
    Handle user registration
    """
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Basic validation
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'registration/signup.html')
        
        if len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters long')
            return render(request, 'registration/signup.html')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists')
            return render(request, 'registration/signup.html')
        
        try:
            # Create user
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
            messages.success(request, f'Welcome to CNCraft, {first_name}! Your account has been created.')
            
            return redirect('profile')
            
        except Exception as e:
            messages.error(request, 'An error occurred while creating your account. Please try again.')
    
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
    
    # Redirect to homepage or wherever they came from
    next_page = request.GET.get('next', 'home')
    return redirect(next_page)

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
