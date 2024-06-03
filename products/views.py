from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product, ShoeType
from home.forms import RegistrationForm, LoginForm
from utils import handle_login, handle_registration

from django.db.models.functions import Lower
from django.core.paginator import Paginator


def products_list(request, department):
    """A view for rendering the products in the store along filtering and sorting."""
    products = Product.objects.filter(
        department__friendly_url_name=department
    )

    query = None
    direction = None
    shoe_type = request.GET.get('shoe_type', 'all')

    # Filter products by shoe type
    if shoe_type and shoe_type != 'all':
        products = products.filter(
            shoe_type__friendly_url_name=shoe_type
        )
        shoe_type = ShoeType.objects.get(
            friendly_url_name=shoe_type
        )

    # Sort products by name or price
    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(
                lower_name=Lower('name')
            )

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

    # Filter products by search query
    if 'search_query' in request.GET:
        query = request.GET['search_query']
        if not query:
            messages.error(request,
                           "Please enter a valid search query!"
                           )
            redirect('products-list', department)

        products = products.filter(name__icontains=query)

    # Pagination
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

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
        'products': page_obj,

    })
