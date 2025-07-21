from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product, Category

def all_products(request):
    """A view to show all products, including sorting and search queries"""
    
    products = Product.objects.all()
    categories = Category.objects.all()
    query = None
    category_filter = None
    sort = None
    direction = None
    price_range = None
    
    # Handle search query
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect('products')
        
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)
    
    # Handle category filtering
    if 'category' in request.GET:
        category_filter = request.GET['category']
        if category_filter:
            products = products.filter(category__name=category_filter)
    
    # Handle price range filtering
    if 'price_range' in request.GET:
        price_range = request.GET['price_range']
        if price_range:
            if price_range == '0-100':
                products = products.filter(price__lte=100)
            elif price_range == '100-500':
                products = products.filter(price__gte=100, price__lte=500)
            elif price_range == '500-1000':
                products = products.filter(price__gte=500, price__lte=1000)
            elif price_range == '1000+':
                products = products.filter(price__gte=1000)
    
    # Handle sorting
    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        
        if sortkey == 'name':
            sortkey = 'name'
        elif sortkey == '-name':
            sortkey = '-name'
        elif sortkey == 'price':
            sortkey = 'price'
        elif sortkey == '-price':
            sortkey = '-price'
        elif sortkey == '-created_at':
            sortkey = '-created_at'
        
        products = products.order_by(sortkey)
    else:
        # Default sorting
        products = products.order_by('name')
    
    # Store total count before pagination
    total_products = products.count()
    
    # Pagination
    paginator = Paginator(products, 12)  # Show 12 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {
        'products': products,
        'categories': categories,
        'search_term': query,
        'current_category': category_filter,
        'current_sorting': sort,
        'current_price_range': price_range,
        'total_products': total_products,
        'is_paginated': products.has_other_pages(),
        'page_obj': products,
    }

    return render(request, 'products/product_list.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    
    product = get_object_or_404(Product, pk=product_id)
    
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
