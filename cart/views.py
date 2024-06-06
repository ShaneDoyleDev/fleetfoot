from django.shortcuts import render, redirect

from home.forms import RegistrationForm, LoginForm
from utils import handle_login, handle_registration


def view_cart(request):
    # request.session.clear()
    """A view for rendering the cart contents."""
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

    return render(request, 'cart/cart.html', {
        'login_form': login_form,
        'registration_form': registration_form,
    })


def add_to_cart(request, product_id):
    """A view for adding an item with a specified
     size and quantity to the shopping cart."""
    quantity = int(request.POST['quantity'])
    size = str(request.POST.get('size'))
    redirect_url = request.POST['redirect_url']
    cart = request.session.get('cart', [])

    # Check if the item already exists in the cart and update quantity
    for item in cart:
        if item['id'] == product_id and item['size'] == size:
            item['quantity'] += quantity
            break
    else:
        cart.append({'id': product_id, 'size': size,
                    'product': product_id, 'quantity': quantity})

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, product_id):
    """A view for adjusting the quantity of a product in the shopping cart or removing it."""
    action = request.POST.get('action')
    size = str(request.POST.get('size'))
    cart = request.session.get('cart', [])

    # Find the cart item that matches the product_id and size
    product = None
    for item in cart:
        if item['id'] == product_id and item['size'] == size:
            product = item
            break

    if product is not None:
        if action == 'remove':
            # Remove the product from the cart
            cart.remove(product)
        else:
            # Adjust the product quantity
            quantity = int(request.POST.get('quantity'))
            product['quantity'] = quantity

    request.session['cart'] = cart

    return redirect('view-cart')
