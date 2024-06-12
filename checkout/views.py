from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.views.decorators.http import require_POST
import json

from cart.context_processors import cart as cart_contents
from checkout.forms import OrderForm
from checkout.models import Order, OrderLineItem
from profiles.models import Profile
from profiles.forms import ProfileForm
from home.forms import RegistrationForm, LoginForm
from products.models import Product, ProductStock, Size
from utils import handle_login, handle_registration

import stripe


@require_POST
def cache_checkout_data(request):
    """
    Cache the checkout data and modify the associated Stripe PaymentIntent.
    """
    try:
        data = json.loads(request.body)
        payment_intent_id = data.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(payment_intent_id, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'username': request.user.username,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """A view for rendering the store checkout."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            payment_intent_id = request.POST.get(
                'payment_intent_client_secret').split('_secret')[0]
            order.stripe_pid = payment_intent_id
            order.original_cart = json.dumps(cart)
            order.save()
            for item in cart:
                try:
                    product = Product.objects.get(id=item['id'])
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item['quantity'],
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

        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_fullname,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
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


def checkout_success(request, order_number):
    """
    Handle successful checkouts and show the order details.
    """
    order = get_object_or_404(Order, order_number=order_number)

    cart = request.session.get('cart', {})

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        profile_data = {
            'default_fullname': order.full_name,
            'default_email': order.email,
            'default_phone_number': order.phone_number,
            'default_country': order.country,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = ProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    # Decrement the quantity of stock from each product in the cart
    for item in cart:
        product = Product.objects.get(id=item['id'])
        size = Size.objects.get(
            department=product.department.id, size=item['size'])
        product_stock = ProductStock.objects.get(
            product=item['product'], size=size
        )
        product_stock.stock -= int(item['quantity'])
        product_stock.save()

    message = mark_safe(f"Order successfully processed! </br> A confirmation email will be sent to <strong>{
                        order.email}</strong>.")
    messages.success(request, message)

    if 'cart' in request.session:
        del request.session['cart']

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

    return render(request, 'checkout/checkout-success.html', {
        'login_form': login_form,
        'registration_form': registration_form,
        'order': order,
    })
