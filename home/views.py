from django.shortcuts import render
from products.models import Product

# View function to render the index page
def index(request):
    """A view to return the index page"""
    
    # Get 3 random products for the homepage (randomized each load)
    featured_products = Product.objects.order_by('?')[:3]
    
    context = {
        'featured_products': featured_products,
    }
    
    # Render and return the 'home/index.html' template
    return render(request, 'home/index.html', context)
