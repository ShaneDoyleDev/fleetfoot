from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm


def home(request):
    """A view for rendering the homepage and authenticating the user."""
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
        'registration_form': registration_form
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
