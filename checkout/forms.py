from django import forms
from checkout.models import Order


class OrderForm(forms.ModelForm):
    """
    A form for creating or updating an order.
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)
