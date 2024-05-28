from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm


def home(request):
    """A view for rendering the homepage and authenticating the user."""
    # Handle User Login
    if request.method == 'POST':
        print("error logging in")
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"Welcome {username}. You have been logged in.")
                return redirect('home')
            else:
                messages.error(
                    request, "There was an error logging in. Please try again!")
                return redirect('home')
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})
    return render(request, 'home/index.html')


def register(request):
    """View for user registration."""
    pass


def user_logout(request):
    """View for user logout."""
    pass
