from django.contrib.auth import authenticate, login
from django.contrib import messages
from home.forms import LoginForm, RegistrationForm


def handle_login(request):
    """
    Handles the login functionality.
    """
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember_me']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)
            messages.success(request,
                             f"Welcome {username.capitalize()}. "
                             "You are logged in.")
            return True
    messages.error(request,
                   "There was an error logging in. Please try again!"
                   )
    return False


def handle_registration(request):
    """
    Handles the registration process for a user.
    """
    registrationForm = RegistrationForm(request.POST)
    if registrationForm.is_valid():
        registrationForm.save()
        messages.success(request, "You have been successfully registered.")
        return True
    messages.error(
        request,
        "There was an error with your registration. Please try again!"
    )
    return False
