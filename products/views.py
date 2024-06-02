from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product, ShoeType
from home.forms import RegistrationForm, LoginForm
from utils import handle_login, handle_registration


def products_list(request, department):
    """A view for rendering the products in the store along filtering and sorting."""
    products = Product.objects.filter(
        department__friendly_url_name=department
    )

    # Authentication
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

    else:
        login_form = LoginForm()
        registration_form = RegistrationForm()

    return render(request, 'products/products-list.html', {
        'login_form': login_form,
        'registration_form': registration_form,
        'department': department,
        'products': products
    })
