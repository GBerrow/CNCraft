from django.shortcuts import render
from products.models import Product

# View function to render the index page
def index(request):
    """A view to return the index page"""
    
    # Get featured products for the homepage
    featured_products = Product.objects.filter(featured=True)[:4]
    
    context = {
        'featured_products': featured_products,
    }
    
    # Render and return the 'home/index.html' template
    return render(request, 'home/index.html', context)
