from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from products.models import Product
import json

def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the cart"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    
    # Get cart from session first, then from cookies if empty
    cart = request.session.get('cart', {})
    if not cart:
        persistent_cart = request.COOKIES.get('persistent_cart', '{}')
        try:
            cart = json.loads(persistent_cart)
        except (json.JSONDecodeError, TypeError):
            cart = {}

    item_id_str = str(item_id)
    if item_id_str in cart:
        # Handle existing item - check format and update accordingly
        if isinstance(cart[item_id_str], dict):
            cart[item_id_str]['quantity'] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id_str]["quantity"]}')
        elif isinstance(cart[item_id_str], list):
            # Convert list format to dict format
            cart[item_id_str] = {'quantity': quantity}
            messages.success(request, f'Updated {product.name} quantity to {quantity}')
        else:
            # Handle integer format
            cart[item_id_str] = {'quantity': int(cart[item_id_str]) + quantity}
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id_str]["quantity"]}')
    else:
        cart[item_id_str] = {'quantity': quantity}
        messages.success(request, f'Added {product.name} to your cart')

    # Save to session
    request.session['cart'] = cart
    
    # Also save to persistent cookie
    response = redirect(redirect_url)
    response.set_cookie('persistent_cart', json.dumps(cart), max_age=30 * 24 * 60 * 60)  # 30 days
    return response

def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    cart = request.session.get('cart', {})
    if not cart:
        persistent_cart = request.COOKIES.get('persistent_cart', '{}')
        try:
            cart = json.loads(persistent_cart)
        except (json.JSONDecodeError, TypeError):
            cart = {}
    
    item_id_str = str(item_id)
    try:
        quantity = int(request.POST.get('quantity'))
    except (TypeError, ValueError):
        messages.error(request, "Invalid quantity.")
        return redirect('view_cart')

    if quantity > 0:
        if item_id_str in cart:
            # Handle different cart item formats
            if isinstance(cart[item_id_str], dict):
                cart[item_id_str]['quantity'] = quantity
            elif isinstance(cart[item_id_str], list):
                # Convert list format to dict format
                cart[item_id_str] = {'quantity': quantity}
            else:
                # Convert integer format to dict format
                cart[item_id_str] = {'quantity': quantity}
            messages.success(request, "Cart updated.")
        else:
            messages.error(request, "Item not found in cart.")
    else:
        if cart.pop(item_id_str, None) is not None:
            messages.success(request, "Item removed from cart.")
        else:
            messages.error(request, "Item not found in cart.")
    
    # Save to session
    request.session['cart'] = cart
    
    # Also save to persistent cookie
    response = redirect('view_cart')
    response.set_cookie('persistent_cart', json.dumps(cart), max_age=30 * 24 * 60 * 60)  # 30 days
    return response

def remove_cart(request, item_id):
    """Remove the item from the cart"""
    cart = request.session.get('cart', {})
    if not cart:
        persistent_cart = request.COOKIES.get('persistent_cart', '{}')
        try:
            cart = json.loads(persistent_cart)
        except (json.JSONDecodeError, TypeError):
            cart = {}
    
    item_id_str = str(item_id)
    if cart.pop(item_id_str, None) is not None:
        messages.success(request, "Item removed from cart.")
    else:
        messages.error(request, "Item not found in cart.")
    
    # Save to session
    request.session['cart'] = cart
    
    # Also save to persistent cookie
    response = redirect('view_cart')
    response.set_cookie('persistent_cart', json.dumps(cart), max_age=30 * 24 * 60 * 60)  # 30 days
    return response
