from django.shortcuts import render, redirect

from home.forms import RegistrationForm, LoginForm
from utils import handle_login, handle_registration


def view_cart(request):
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
