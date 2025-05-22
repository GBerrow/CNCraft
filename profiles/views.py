from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
