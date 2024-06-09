from django.shortcuts import render


def profile(request):
    """Display the users profile information."""
    return render(request, 'profiles/profile.html', {})
