import uuid

from django.conf import settings
from django.db import models
from django.db.models import Sum
from products.models import Product
from profiles.models import Profile

from django_countries.fields import CountryField


class Order(models.Model):
    """
    Represents an order placed by a customer.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """Generate a random unique order number for the order"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates the total cost of the order, including the order total,
        delivery cost, and grand total each time a line item is added.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * \
                settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        If the `order_number` field is not set, it generates an order number
        using the `_generate_order_number` method before saving the instance.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the order.
        """
        return f'Order number: {self.order_number}'


class OrderLineItem(models.Model):
    """
    Represents an individual line item in an order.
    """

    order = models.ForeignKey(Order, null=False,
                              blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False,
        on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        """
        Calculates the lineitem_total before saving.
        """
        self.lineitem_total = self.product.current_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the line item.
        """
        return f'SKU {self.product.sku} on order {self.order.order_number}'
