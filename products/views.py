import random

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from products.forms import ProductForm, ProductStockForm
from home.forms import RegistrationForm, LoginForm
from products.models import Product, ShoeType
from utils import handle_login, handle_registration


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
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if request.method == 'POST':
        form_type = request.POST['form_type']

        # Handle User Login
        if form_type == "login_form":
            if handle_login(request):
                redirect('products-list', department)

        # Handle User Registration
        elif form_type == 'registration_form':
            if handle_registration(request):
                redirect('products-list', department)

    return render(request, 'products/products-list.html', {
        'login_form': login_form,
        'registration_form': registration_form,
        'department': department,
        'shoe_type': shoe_type,
        'products': page_obj,
    })


def product_detail(request, product_id):
    """A view for rendering out an individual product
    with more detailed information."""
    product = get_object_or_404(Product, pk=product_id)

    # Select a random shoe from the same brand
    related_products = Product.objects.filter(
        brand=product.brand,
        department__name=product.department.name
    ).exclude(id=product_id)
    related_product = random.choice(
        related_products) if related_products else None

    product_sizes = [size.size for size in product.sizes.all()]

    # Authentication
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if request.method == 'POST':
        form_type = request.POST['form_type']

        # Handle User Login
        if form_type == "login_form":
            if handle_login(request):
                redirect('product-detail', product_id)

        # Handle User Registration
        elif form_type == 'registration_form':
            if handle_registration(request):
                redirect('product-detail', product_id)

    return render(request, 'products/product-detail.html', {
        'login_form': login_form,
        'registration_form': registration_form,
        'product': product,
        'related_product': related_product,
        'product_sizes': product_sizes
    })


def admin_check(user):
    return user.is_superuser


@login_required
@user_passes_test(admin_check)
def add_product(request):
    """
    Add a new product to the database.
    """
    if request.method == 'POST':
        productForm = ProductForm(request.POST, request.FILES)

        if productForm.is_valid():
            productForm.save()
            messages.success(request, 'Product added successfully.')
            return redirect('add-product')
        else:
            messages.error(
                request, 'There was an error with your submission. Please check the form and try again.')
    else:
        productForm = ProductForm()
    return render(request, 'products/add-product.html', {
        'product_form': productForm,
    })


@login_required
@user_passes_test(admin_check)
def update_stock(request):
    """
    Add update the stock of an existing product in the database.
    """
    if request.method == 'POST':
        product_stock_form = ProductStockForm(request.POST, request.FILES)

        if product_stock_form.is_valid():
            product_stock_form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('add-product')
        else:
            messages.error(
                request, 'There was an error with your submission. Please check the form and try again.')
    else:
        product_stock_form = ProductStockForm()
    return render(request, 'products/update-stock.html', {
        'product_stock_form': product_stock_form,
    })
