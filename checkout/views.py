from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from cart.contexts import cart_contents

def checkout(request):
    """
    Handle the checkout process
    """

    # Get the cart from the session
    cart = request.session.get('cart', {})
    # If the cart is empty, redirect to products page with an error message
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    # Get current cart contents and total
    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    
    # Create a blank order form
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_placeholder',  # Placeholder for Stripe public key
        'client_secret': 'test_secret_placeholder',  # Placeholder for Stripe client secret
        'cart_items': current_cart['cart_items'],
        'total': current_cart['total'],
        'delivery': current_cart['delivery'],
        'grand_total': current_cart['grand_total'],
        'product_count': current_cart['product_count'],
    }

    # Render the checkout page with the context
    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    # Retrieve the order by order number, or return 404 if not found
    order = get_object_or_404(Order, order_number=order_number)
    
    # If the user is authenticated, attach their profile to the order
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

    # Display a success message to the user
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Remove the cart from the session as the order is complete
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    # Render the checkout success page with the order details
    return render(request, template, context)
