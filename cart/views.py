from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the cart"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    item_id_str = str(item_id)
    if item_id_str in cart:
        cart[item_id_str]['quantity'] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id_str]["quantity"]}')
    else:
        cart[item_id_str] = {'quantity': quantity}
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    cart = request.session.get('cart', {})
    item_id_str = str(item_id)
    try:
        quantity = int(request.POST.get('quantity'))
    except (TypeError, ValueError):
        messages.error(request, "Invalid quantity.")
        return redirect('view_cart')

    if quantity > 0:
        if item_id_str in cart:
            cart[item_id_str]['quantity'] = quantity
            messages.success(request, "Cart updated.")
        else:
            messages.error(request, "Item not found in cart.")
    else:
        if cart.pop(item_id_str, None) is not None:
            messages.success(request, "Item removed from cart.")
        else:
            messages.error(request, "Item not found in cart.")
    request.session['cart'] = cart
    return redirect('view_cart')

def remove_cart(request, item_id):
    """Remove the item from the cart"""
    cart = request.session.get('cart', {})
    item_id_str = str(item_id)
    if cart.pop(item_id_str, None) is not None:
        messages.success(request, "Item removed from cart.")
    else:
        messages.error(request, "Item not found in cart.")
    request.session['cart'] = cart
    return redirect('view_cart')
