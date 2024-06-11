import random

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from products.forms import ProductForm, ProductStockForm
from profiles.forms import ReviewForm, RatingForm
from home.forms import RegistrationForm, LoginForm
from products.models import Product, ShoeType
from profiles.models import Review, Rating
from utils import handle_login, handle_registration


def admin_check(user):
    """
    Checks if the user is an admin.
    """
    return user.is_superuser


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
    with more detailed information and reviews."""
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)

    # Authentication
    login_form = LoginForm()
    registration_form = RegistrationForm()

    # Review and Rating
    review_form = ReviewForm()
    rating_form = RatingForm()

    average_rating = round(Rating.objects.filter(review__product=product).aggregate(
        average_score=Avg('score'))['average_score'] or 0)

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

        # Handle Review and Rating
        elif form_type == 'review_form':
            review_form = ReviewForm(request.POST)
            rating_form = RatingForm(request.POST)
            if review_form.is_valid() and rating_form.is_valid():
                review = review_form.save(commit=False)
                review.user_profile = request.user.profile
                review.product = product
                review.save()
                rating = rating_form.save(commit=False)
                rating.review = review
                rating.save()
                messages.success(
                    request, 'Thank you for submitting a review!')
                return redirect('product-detail', product_id=product.id)
            else:
                messages.error(
                    request, 'There was an error with your review. Please try again.')
    else:
        review_form = ReviewForm()
        rating_form = RatingForm()

    return render(request, 'products/product-detail.html', {
        'login_form': login_form,
        'registration_form': registration_form,
        'review_form': review_form,
        'rating_form': rating_form,
        'product': product,
        'average_rating': average_rating,
        'related_product': related_product,
        'product_sizes': product_sizes,
        'reviews': reviews,
    })


@login_required
@user_passes_test(admin_check)
def product_admin(request):
    """
    Add a new product or update the stock of an existing product in the database.
    """
    product_form = ProductForm()
    product_stock_form = ProductStockForm()

    if request.method == 'POST':
        if request.POST['form_type'] == 'add_product_form':
            product_form = ProductForm(request.POST, request.FILES)
            if product_form.is_valid():
                product_form.save()
                messages.success(request, 'Product added successfully.')
                return redirect('product-admin')
            else:
                messages.error(
                    request, 'There was an error with your submission. Please check the form and try again.')
        elif request.POST['form_type'] == 'update_stock_form':
            product_stock_form = ProductStockForm(request.POST, request.FILES)
            if product_stock_form.is_valid():
                product_stock_form.save()
                messages.success(
                    request, 'Product stock updated successfully.')
                return redirect('product-admin')
            else:
                messages.error(
                    request, 'There was an error with your submission. Please check the form and try again.')

    return render(request, 'products/product-admin.html', {
        'product_form': product_form,
        'product_stock_form': product_stock_form,
    })


@login_required
@user_passes_test(admin_check)
def product_update(request, product_id):
    """
    Update an existing product in the database.
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('product-detail', product_id=product.id)
        else:
            messages.error(
                request, 'There was an error with your submission. Please check the form and try again.')
    else:
        product_form = ProductForm(instance=product)
    return render(request, 'products/product-update.html', {
        'product': product,
        'product_form': product_form
    })


def product_delete(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted!')
    return redirect('home')
