import time
import json

from django.http import HttpResponse
from profiles.models import Profile
from products.models import Product
from checkout.models import Order, OrderLineItem

import stripe


class StripeWebhookHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        payment_intent = event.data.object
        payment_intent_id = payment_intent.id
        cart = json.loads(payment_intent.metadata.cart)

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            payment_intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = payment_intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information
        profile = None
        username = payment_intent.metadata.username
        if username != 'AnonymousUser':
            profile = Profile.objects.get(user__username=username)
            profile.default_full_name = shipping_details.name
            profile.default_email = billing_details.email
            profile.default_phone_number = shipping_details.phone
            profile.default_country = shipping_details.address.country
            profile.default_postcode = shipping_details.address.postal_code
            profile.default_town_or_city = shipping_details.address.city
            profile.default_street_address1 = shipping_details.address.line1
            profile.default_street_address2 = shipping_details.address.line2
            profile.default_county = shipping_details.address.state
            profile.save()

        # Check if order already exists in the database
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=payment_intent_id,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {
                    event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            # If order does not exist in the database then create it
            order = None
            try:
                order = Order.objects.create(
                    user_profile=profile,
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=payment_intent_id,
                )
                for item in cart:
                    product = Product.objects.get(id=item['id'])
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item['quantity'],
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {
                event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
