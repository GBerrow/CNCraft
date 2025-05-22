from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    
    if request.GET:
        # Handle sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                # Annotate products with lowercase name for case-insensitive sorting
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                # Sort by category name
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    # Prefix with '-' for descending order
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        # Handle category filtering
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            
        # Handle search queries
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # Show error if search box is empty
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # Search in name or description fields
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
    # Store current sorting for template use
    current_sorting = f'{sort}_{direction}' if sort and direction else None
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    
    return render(request, 'products/shop.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """
    
    # Get the product by ID or return 404 if not found
    product = get_object_or_404(Product, pk=product_id)
    
    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)

def products_by_category(request, category_id):
    """ A view to show products filtered by category """
    
    # Get the category by ID or return 404 if not found
    category = get_object_or_404(Category, pk=category_id)
    # Filter products by the selected category
    products = Product.objects.filter(category=category)
    
    context = {
        'category': category,
        'products': products,
    }
    
    return render(request, 'products/shop.html', context)
