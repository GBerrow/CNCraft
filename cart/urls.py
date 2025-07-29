from django.urls import path
from . import views

# Define URL patterns for the cart app
urlpatterns = [
    # View the cart
    path('', views.view_cart, name='view_cart'),
    # Add a product to the cart
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),  # New line added
    # Adjust the quantity of a product in the cart
    path('adjust/<int:item_id>/', views.adjust_cart, name='adjust_cart'),
    # Remove a product from the cart
    path('remove/<int:item_id>/', views.remove_cart, name='remove_cart'),
]