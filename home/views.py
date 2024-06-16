import random
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from home.forms import RegistrationForm, LoginForm
from products.models import Product
from utils import handle_login, handle_registration


def home(request):
    """A view for rendering the homepage and authenticating the user."""

    latest_products = Product.objects.order_by('-created_at')[:4]
    sale_products = Product.objects.filter(on_sale=True)
    sale_products = random.sample(
        list(sale_products), min(len(sale_products), 4)
    )

    # Authentication
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if request.method == 'POST':
        form_type = request.POST['form_type']

        # Handle User Login
        if form_type == "login_form":
            if handle_login(request):
                return redirect('home')

        # Handle User Registration
        elif form_type == 'registration_form':
            if handle_registration(request):
                return redirect('home')

    return render(request, 'home/index.html', {
        'login_form': login_form,
        'registration_form': registration_form,
        'latest_products': latest_products,
        'sale_products': sale_products,
    })


def user_logout(request):
    """View for user logout."""
    logout(request)
    messages.success(
        request, "You have been logged out.")
    return redirect('home')
