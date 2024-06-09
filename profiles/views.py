from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from profiles.models import Profile
from profiles.forms import ProfileForm


def profile(request):
    """Display the users profile information."""
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        print('called')
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(
                request, "You have successfully updated your profile.")
    orders = profile.orders.all()
    profile_form = ProfileForm(instance=profile)

    return render(request, 'profiles/profile.html', {
        'profile': profile,
        'orders': orders,
        'profile_form': profile_form
    })
