from django.urls import path
from . import views

# Define URL patterns for the checkout app
urlpatterns = [
    # URL for the checkout page
    path('', views.checkout, name='checkout'),
    # URL for the checkout success page, expects an order_number parameter
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    # URL for Stripe webhooks
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
]