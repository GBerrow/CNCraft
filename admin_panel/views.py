from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from products.models import Product
from checkout.models import Order

# Decorators for staff-only access
def staff_required(view_func):
    decorated_view = login_required(user_passes_test(lambda u: u.is_staff)(view_func))
    return decorated_view

@method_decorator(staff_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'admin_panel/dashboard_overview.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_orders'] = Order.objects.count()
        context['total_users'] = User.objects.count()
        context['total_products'] = Product.objects.count()
        # Add placeholder for revenue
        context['total_revenue'] = "10,000.00"  # Placeholder
        return context

@method_decorator(staff_required, name='dispatch')
class OrderListView(ListView):
    model = Order
    template_name = 'admin_panel/orders.html'
    context_object_name = 'orders'
    paginate_by = 10
    ordering = ['-date']

@method_decorator(staff_required, name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'admin_panel/products.html'
    context_object_name = 'products'
    paginate_by = 10
    ordering = ['name']

@method_decorator(staff_required, name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'admin_panel/users.html'
    context_object_name = 'users'
    paginate_by = 10
    ordering = ['-date_joined'] 