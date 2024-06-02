import random
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from home.forms import RegistrationForm, LoginForm
from products.models import Product


def home(request):
    """A view for rendering the homepage and authenticating the user."""

    latest_products = Product.objects.order_by('-created_at')[:4]
    sale_products = random.sample(
        list(Product.objects.filter(on_sale=True)), 4
    )

    # Authentication
    if request.method == 'POST':
        form_type = request.POST['form_type']

        # Handle User Login
        if form_type == "login_form":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                remember_me = form.cleaned_data['remember_me']
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    # Set login expiry session for 2 weeks
                    if remember_me:
                        request.session.set_expiry(1209600)
                    else:
                        request.session.set_expiry(0)
                    messages.success(request, f"Welcome {
                                     username.capitalize()}. You have been logged in.")
                    return redirect('home')
                else:
                    messages.error(
                        request, "There was an error logging in. Please try again!")
                    return redirect('home')

        # Handle User Registration
        elif form_type == 'registration_form':
            registrationForm = RegistrationForm(request.POST)
            if registrationForm.is_valid():
                registrationForm.save()
                messages.success(
                    request, "You have been successfully registered.")
                return redirect('home')
            else:
                messages.success(
                    request, "There was an error with your registration. Please try again!")
                return redirect('home')

    else:
        login_form = LoginForm()
        registration_form = RegistrationForm()

    return render(request, 'home/index.html', {
        'login_form': login_form,
        'registration_form': registration_form,
        'latest_products': latest_products,
        'sale_products': sale_products,
    })


def register(request):
    """View for user registration."""
    pass


def user_logout(request):
    """View for user logout."""
    logout(request)
    messages.success(
        request, "You have been logged out.")
    return redirect('home')
