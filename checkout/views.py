from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from cart.context_processors import cart as cart_contents
from checkout.forms import OrderForm
from checkout.models import Order, OrderLineItem
from home.forms import RegistrationForm, LoginForm
from products.models import Product
from utils import handle_login, handle_registration

import stripe


def checkout(request):
    """A view for rendering the store checkout."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save()
            for item in cart:
                try:
                    product = Product.objects.get(id=item.id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item.quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our database.")
                    )
                    order.delete()
                    return redirect(reverse('view-cart'))

            return redirect(reverse('checkout-success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, "There's nothing in your cart at the moment.")
            return redirect(reverse('home'))

        # Setup and create the stripe payment intent
        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        payment_intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

    order_form = OrderForm()

    # Authentication
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if request.method == 'POST':
        form_type = request.POST['form_type']

        # Handle User Login
        if form_type == "login_form":
            if handle_login(request):
                return redirect('checkout')

        # Handle User Registration
        elif form_type == 'registration_form':
            if handle_registration(request):
                return redirect('checkout')

    return render(request, 'checkout/checkout.html', {
        'login_form': login_form,
        'registration_form': registration_form,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'payment_intent_client_secret': payment_intent.client_secret,
    })
