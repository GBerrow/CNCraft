from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        # Specify the model and fields to include in the form
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # Define placeholder text for each field
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
            'postcode': 'Postal Code',
            'country': 'Country',
        }

        # Set autofocus on the 'full_name' field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Define autocomplete attributes for each field
        autocomplete_attrs = {
            'full_name': 'name',
            'email': 'email',
            'phone_number': 'tel',
            'street_address1': 'street-address',
            'street_address2': 'street-address',
            'town_or_city': 'address-level2',
            'county': 'address-level1',
            'postcode': 'postal-code',
            'country': 'country',
        }

        # Loop through each field in the form
        for field in self.fields:
            # Add an asterisk to required fields' placeholders
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # Set the placeholder attribute
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add a CSS class for styling
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Add autocomplete attribute
            if field in autocomplete_attrs:
                self.fields[field].widget.attrs['autocomplete'] = autocomplete_attrs[field]
            # Remove the default label
            self.fields[field].label = False