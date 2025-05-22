from django.urls import path
from . import views

# Define URL patterns for the products app
urlpatterns = [
    # URL for displaying all products
    path('', views.all_products, name='products'),
    # URL for displaying details of a specific product by its ID
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    # URL for displaying products filtered by category ID
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),
]