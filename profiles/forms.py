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

        # Iterate through all fields in the form
        for field in self.fields:
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
            # Remove the label for each field
            self.fields[field].label = False