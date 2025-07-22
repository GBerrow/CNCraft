from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserProfileForm
from .models import UserProfile
from checkout.models import Order

@login_required
def profile(request):
    """ Display the user's profile. """
    # Get the user's profile or return 404 if not found
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # If the form is submitted, populate it with POST data and the current profile instance
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

    template = 'profiles/dashboard.html'
    context = {
        'form': form,
        'orders': orders,
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
