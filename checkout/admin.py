from django.contrib import admin
from .models import Order, OrderLineItem

# Inline admin descriptor for OrderLineItem model
# Used in the Order admin interface to display line items inline
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    # Make lineitem_total field read-only in the admin
    readonly_fields = ('lineitem_total',)

# Admin interface customization for the Order model
class OrderAdmin(admin.ModelAdmin):
    # Display OrderLineItems inline within the Order admin page
    inlines = (OrderLineItemAdminInline,)

    # Fields that are read-only in the admin
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    # Fields to display in the admin form for Order
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid')

    # Fields to display in the Order list view
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # Default ordering for the Order list view (most recent first)
    ordering = ('-date',)

# Register the Order model with the customized admin interface
admin.site.register(Order, OrderAdmin)
