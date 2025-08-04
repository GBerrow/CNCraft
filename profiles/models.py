from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Model to store additional user information for delivery and order history
class UserProfile(models.Model):
    """
    User profile model for maintaining delivery information
    and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=40, null=True, blank=True)
    default_email_notifications = models.BooleanField(default=False)
    default_order_status_updates = models.BooleanField(default=False)
    default_promotional_emails = models.BooleanField(default=False)
    default_newsletter_subscription = models.BooleanField(default=False)
    
    # E-commerce preferences
    currency = models.CharField(max_length=3, default='USD', choices=[
        ('USD', 'USD ($)'),
        ('EUR', 'EUR (€)'),
        ('GBP', 'GBP (£)'),
        ('CAD', 'CAD (C$)'),
    ])
    language = models.CharField(max_length=2, default='en', choices=[
        ('en', 'English'),
        ('es', 'Español'),
        ('fr', 'Français'),
        ('de', 'Deutsch'),
    ])
    display_mode = models.CharField(max_length=10, default='light', choices=[
        ('light', 'Light'),
        ('dark', 'Dark'),
        ('auto', 'Auto'),
    ])
    cart_auto_save = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username

# Signal receiver to create or update user profile upon user save
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        # Create a new user profile if a new user is created
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
