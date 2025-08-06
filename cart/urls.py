from django.urls import path
from . import views

# Define URL patterns for the cart app
urlpatterns = [
    # View the cart
    path('', views.view_cart, name='view_cart'),
    # Add a product to the cart
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    # Adjust the quantity of a product in the cart
    path('adjust/<int:item_id>/', views.adjust_cart, name='adjust_cart'),
    # Remove a product from the cart
    path('remove/<int:item_id>/', views.remove_cart, name='remove_cart'),
    # Get cart count for AJAX updates
    path('get_count/', views.get_cart_count, name='get_cart_count'),
    # Clear all items from cart
    path('clear_all/', views.clear_all_cart, name='clear_all_cart'),
]