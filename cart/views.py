from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    """
    Add a quantity of the specified product to the shopping cart.

    Retrieves the product, quantity, and redirect URL from the request.
    Updates the cart in the session, adding or updating the product quantity.
    """
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # If product already in cart, increment quantity
    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')
    else:
        # Otherwise, add product to cart
        cart[product_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    # Save updated cart to session
    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, product_id):
    """
    Adjust the quantity of the specified product to the specified amount.

    If quantity > 0, update the quantity.
    If quantity <= 0, remove the product from the cart.
    """
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        # Update product quantity in cart
        cart[product_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[product_id]}')
    else:
        # Remove product from cart if quantity is zero or less
        cart.pop(product_id)
        messages.success(request, f'Removed {product.name} from your cart')

    # Save updated cart to session
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, product_id):
    """
    Remove the item from the shopping cart.

    Attempts to remove the product from the cart and returns an HTTP response.
    """
    try:
        product = get_object_or_404(Product, pk=product_id)
        cart = request.session.get('cart', {})

        # Remove product from cart
        cart.pop(product_id)
        messages.success(request, f'Removed {product.name} from your cart')

        # Save updated cart to session
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        # Handle errors and return error response
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
