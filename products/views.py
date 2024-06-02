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

    query = None
    shoe_type = None
    if request.method == 'GET':
        if 'shoe_type' in request.GET:
            products = products.filter(
                shoe_type__friendly_url_name=request.GET['shoe_type']
            )
            shoe_type = ShoeType.objects.get(
                friendly_url_name=request.GET['shoe_type']
            )

        if 'search_query' in request.GET:
            query = request.GET['search_query']
            if not query:
                messages.error(request, "Please enter a valid search query!")
                redirect('products-list', department)

            products = products.filter(name__icontains=query)

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
        'shoe_type': shoe_type,
        'products': products
    })
