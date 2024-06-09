from django.shortcuts import render, get_object_or_404
from profiles.models import Profile


def profile(request):
    """Display the users profile information."""
    profile = get_object_or_404(Profile, user=request.user)

    return render(request, 'profiles/profile.html', {
        'profile': profile
    })
