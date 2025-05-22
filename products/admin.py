from django.contrib import admin
from .models import Category, Product, ProductImage

# Inline admin class for managing product images within the product admin interface
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

# Admin class for managing products with customized display, filtering, search and ordering options
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'discount_price',
        'rating',
        'in_stock',
        'featured',
    )
    
    list_filter = ('category', 'in_stock', 'featured')
    search_fields = ('name', 'description', 'sku')
    ordering = ('name',)
    inlines = [ProductImageInline]

# Admin class for managing product categories with customized display options
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)