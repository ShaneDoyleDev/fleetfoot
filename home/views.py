from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    """A view for rendering the homepage."""
    return render(request, 'home/index.html')


def register(request):
    """View for user registration."""
    pass


def user_login(request):
    """View for user login."""
    pass


def user_logout(request):
    """View for user logout."""
    pass
