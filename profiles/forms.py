from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        # Use the UserProfile model and exclude the 'user' field from the form
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # Define placeholder text for each field
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
            'default_postcode': 'Postal Code',
            'default_country': 'Country',
        }

        # Set autofocus on the phone number field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # Define autocomplete attributes for each field
        autocomplete_attrs = {
            'default_phone_number': 'tel',
            'default_street_address1': 'street-address',
            'default_street_address2': 'street-address',
            'default_town_or_city': 'address-level2',
            'default_county': 'address-level1',
            'default_postcode': 'postal-code',
            'default_country': 'country',
        }

        # Iterate through all fields in the form
        for field in self.fields:
            # Skip notification preference fields (they are checkboxes)
            if field in ['default_email_notifications', 'default_order_status_updates', 
                        'default_promotional_emails', 'default_newsletter_subscription']:
                continue
            
            # Skip e-commerce preference fields (they are choice fields and checkboxes)
            if field in ['currency', 'language', 'display_mode', 'cart_auto_save']:
                continue
                
            if field != 'default_country':
                # Add '*' to placeholder if the field is required
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Set the placeholder attribute
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add a CSS class to each field
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            # Add autocomplete attribute
            if field in autocomplete_attrs:
                self.fields[field].widget.attrs['autocomplete'] = autocomplete_attrs[field]
            # Remove the label for each field
            self.fields[field].label = False

        # Add notification preferences as checkboxes
        self.fields['default_email_notifications'].widget = forms.CheckboxInput()
        self.fields['default_order_status_updates'].widget = forms.CheckboxInput()
        self.fields['default_promotional_emails'].widget = forms.CheckboxInput()
        self.fields['default_newsletter_subscription'].widget = forms.CheckboxInput()