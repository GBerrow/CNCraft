from django.urls import path
from . import views

# Define URL patterns for the profiles app
urlpatterns = [
    # Profile page
    path('', views.profile, name='profile'),
    # Order history page, expects an order_number parameter
    path('order_history/<order_number>', views.order_history, name='order_history'),
    # Authentication URLs
    path('signup/', views.signup_view, name='account_signup'),
    path('login/', views.login_view, name='account_login'),
    path('logout/', views.logout_view, name='account_logout'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
]