from django.shortcuts import render


def home(request):
    """A view for rendering the homepage"""

    return render(request, 'home/index.html')
