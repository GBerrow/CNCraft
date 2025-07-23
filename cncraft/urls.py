from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Define the URL patterns for the project
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    # Custom Admin Panel URLs
    path('admin-panel/', include('admin_panel.urls')),
    # Accounts URLs
    path('accounts/', include('django.contrib.auth.urls')),
    # Home app URLs
    path('', include('home.urls')),
    # Products app URLs
    path('products/', include('products.urls')),
    # Cart app URLs
    path('cart/', include('cart.urls')),
    # Checkout app URLs
    path('checkout/', include('checkout.urls')),
    # Profiles app URLs
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
