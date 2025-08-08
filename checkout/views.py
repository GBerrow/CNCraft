import os
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from cart.contexts import cart_contents
import json
import stripe

# Configure Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    """Handle checkout process"""
    # Check if user just completed an order
    recent_order = request.COOKIES.get('order_completed')
    if recent_order:
        # Remove the cookie and redirect to products
        response = redirect('products')
        response.delete_cookie('order_completed')
        messages.info(request, f"Your order {recent_order} was already completed successfully. You've been redirected to continue shopping.")
        return response
    
    # Get cart from session first
    cart = request.session.get('cart', {})
    
    # If session cart is empty, try to get from persistent cart cookie
    if not cart:
        persistent_cart = request.COOKIES.get('persistent_cart', '{}')
        try:
            cart = json.loads(persistent_cart)
        except (json.JSONDecodeError, TypeError):
            cart = {}
    
    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect(reverse('view_cart'))
    
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            
            # Attach user profile if authenticated
            if request.user.is_authenticated:
                order.user_profile = request.user.userprofile
            
            # Calculate totals
            cart_items = cart_contents(request)
            total = cart_items['grand_total']
            order.order_total = total
            order.delivery_cost = cart_items['delivery']
            order.save()
            
            # Create order line items
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        # Simple quantity format
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    elif isinstance(item_data, list):
                        # Handle list format from persistent cart
                        quantity = 1  # Default quantity
                        for item in item_data:
                            if isinstance(item, dict) and 'quantity' in item:
                                quantity = item['quantity']
                                break
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    elif isinstance(item_data, dict) and 'items_by_size' in item_data:
                        # Size-based format
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                            )
                            order_line_item.save()
                    else:
                        # Fallback for unknown format
                        quantity = 1
                        if isinstance(item_data, dict) and 'quantity' in item_data:
                            quantity = item_data['quantity']
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            
            # Check if we're in test mode (using placeholder keys)
            # Check for placeholder keys
            if (not settings.STRIPE_SECRET_KEY or 
                not settings.STRIPE_PUBLISHABLE_KEY):
                # Test mode - simulate successful payment
                messages.success(request, f'Test order successful! Order number: {order.order_number}')
                # Clear cart immediately after successful order creation
                request.session['cart'] = {}
                if 'cart' in request.session:
                    del request.session['cart']
                # Create response and clear persistent cart
                response = redirect('checkout_success', order_number=order.order_number)
                response.delete_cookie('persistent_cart')
                response.set_cookie('order_completed', order.order_number, max_age=300)  # 5 minutes
                return response
            
            # Real Stripe integration
            try:
                intent = stripe.PaymentIntent.create(
                    amount=int(total * 100),
                    currency=settings.STRIPE_CURRENCY,
                    metadata={
                        'order_number': order.order_number,
                        'user_id': request.user.id if request.user.is_authenticated else None,
                    }
                )
                request.session['payment_intent_id'] = intent.id
                # Clear cart immediately after successful order creation
                request.session['cart'] = {}
                if 'cart' in request.session:
                    del request.session['cart']
                # Create response and clear persistent cart
                response = redirect('checkout_success', order_number=order.order_number)
                response.delete_cookie('persistent_cart')
                response.set_cookie('order_completed', order.order_number, max_age=300)  # 5 minutes
                return response
            except stripe.error.StripeError as e:
                messages.error(request, f'Payment error: {e}')
                order.delete()
                return redirect('view_cart')
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
                order.delete()
                return redirect('view_cart')
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        # Pre-fill form for authenticated users
        if request.user.is_authenticated:
            try:
                profile = request.user.userprofile
                order_form = OrderForm(initial={
                    'full_name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
                    'email': request.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except:
                order_form = OrderForm()
        else:
            order_form = OrderForm()
    
    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect(reverse('view_cart'))
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY,
        'client_secret': None,
    }
    
    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    # Retrieve the order by order number, or return 404 if not found
    order = get_object_or_404(Order, order_number=order_number)
    
    # Ensure order totals are properly calculated
    order.update_total()
    
    # If the user is authenticated, attach their profile to the order
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            # Attach the user's profile to the order
            order.user_profile = profile
            order.save()
        except UserProfile.DoesNotExist:
            # User doesn't have a profile yet, that's okay
            pass

    # Display a success message to the user
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Remove the cart from the session as the order is complete
    if 'cart' in request.session:
        del request.session['cart']
    
    # Clear persistent cart cookie
    response = render(request, 'checkout/checkout_success.html', {'order': order})
    response.delete_cookie('persistent_cart')
    return response

@require_POST
@csrf_exempt
def stripe_webhook(request):
    """
    Handle Stripe webhooks
    """
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        order_number = payment_intent['metadata']['order_number']
        
        # Update order status
        try:
            order = Order.objects.get(order_number=order_number)
            order.stripe_pid = payment_intent['id']
            order.save()
        except Order.DoesNotExist:
            return HttpResponse(status=404)
    
    elif event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        order_number = payment_intent['metadata']['order_number']
        
        # Handle failed payment
        try:
            order = Order.objects.get(order_number=order_number)
            # You might want to send an email notification here
            pass
        except Order.DoesNotExist:
            return HttpResponse(status=404)

    return HttpResponse(status=200)
