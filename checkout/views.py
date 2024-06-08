from django.shortcuts import render, redirect
from django.conf import settings

from cart.context_processors import cart as cart_contents
from checkout.forms import OrderForm
from home.forms import RegistrationForm, LoginForm
from utils import handle_login, handle_registration

import stripe


def checkout(request):
    """A view for rendering the store checkout."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})

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
