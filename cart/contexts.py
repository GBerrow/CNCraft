from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """
    Context processor to make cart contents available in all templates.
    """
    cart_items = []
    total = 0
    product_count = 0
    # Get the cart from the session, or an empty dict if not present
    cart = request.session.get('cart', {})

    # Iterate through cart items
    for product_id, item_data in cart.items():
        # Retrieve the product or return 404 if not found
        product = get_object_or_404(Product, pk=product_id)
        # Get the product's display price
        price = product.get_display_price()
        # Handle both legacy int and new dict format
        if isinstance(item_data, dict):
            quantity = item_data.get('quantity', 1)
        else:
            quantity = item_data
        subtotal = quantity * price
        # Update total cost and product count
        total += subtotal
        product_count += quantity
        # Add item details to cart_items list
        cart_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal,
        })
    
    # Calculate delivery cost and amount needed for free delivery
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    # Calculate grand total
    grand_total = delivery + total
    
    # Prepare context dictionary to return
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context