# /project_data/portalapp/restaurant/forms.py

from django import forms
from .models import Restaurant  # Assuming you have a Restaurant model defined in models.py

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address']  # Adjust fields based on your Restaurant model

# Add any additional form fields or customization as needed
