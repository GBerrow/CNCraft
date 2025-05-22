# Admin interface configuration for the UserProfile model
from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the UserProfile model
    """
    # Fields to display in the list view
    list_display = ('user', 'default_phone_number', 'default_town_or_city', 'default_country')
    # Fields to search in the admin interface search box
    search_fields = ('user__username', 'default_phone_number')
    # Fields to filter the list view by
    list_filter = ('default_country',)


# Register the UserProfileAdmin class with the admin interface
admin.site.register(UserProfile, UserProfileAdmin)
