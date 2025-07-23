from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('users/', views.UserListView.as_view(), name='users'),
] 