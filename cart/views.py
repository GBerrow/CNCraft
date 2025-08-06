from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
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

def get_cart_count(request):
    """AJAX endpoint to get current cart count"""
    # Get cart from session first, then from cookies if empty
    cart = request.session.get('cart', {})
    if not cart:
        persistent_cart = request.COOKIES.get('persistent_cart', '{}')
        try:
            cart = json.loads(persistent_cart)
        except (json.JSONDecodeError, TypeError):
            cart = {}
    
    # Calculate product count
    product_count = 0
    for item_id, item_data in cart.items():
        try:
            # Handle different cart data formats
            if isinstance(item_data, int):
                quantity = item_data
            elif isinstance(item_data, list):
                quantity = 1  # Default quantity
                for item in item_data:
                    if isinstance(item, dict) and 'quantity' in item:
                        quantity = item['quantity']
                        break
            elif isinstance(item_data, dict):
                quantity = item_data.get('quantity', 1)
            else:
                quantity = 1
                
            product_count += quantity
        except:
            continue
    
    # Add CORS headers for AJAX requests
    response = JsonResponse({
        'product_count': product_count,
        'cart_items': len(cart),
        'success': True
    })
    response['Cache-Control'] = 'no-cache'
    return response

def clear_all_cart(request):
    """Clear all items from the cart"""
    if request.method == 'POST':
        # Clear session cart
        request.session['cart'] = {}
        
        # Clear persistent cookie cart
        response = redirect('view_cart')
        response.set_cookie('persistent_cart', '{}', max_age=30 * 24 * 60 * 60)  # 30 days
        
        messages.success(request, "All items have been removed from your cart.")
        return response
    
    return redirect('view_cart')
