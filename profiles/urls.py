from django.urls import path
from . import views

# Define URL patterns for the profiles app
urlpatterns = [
    # Profile page
    path('', views.profile, name='profile'),
    # Order history page, expects an order_number parameter
    path('order_history/<order_number>', views.order_history, name='order_history'),
]