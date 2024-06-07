from django.shortcuts import render, redirect

from checkout.forms import OrderForm
from home.forms import RegistrationForm, LoginForm
from utils import handle_login, handle_registration


def checkout(request):
    """A view for rendering the store checkout."""
    cart = request.session.get('cart', {})

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
        'order_form': order_form
    })
