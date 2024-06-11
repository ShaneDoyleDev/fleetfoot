from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from checkout.models import Order
from profiles.models import Profile, Wishlist
from profiles.forms import ProfileForm


@login_required
def profile(request):
    """Display the users profile information."""
    profile = get_object_or_404(Profile, user=request.user)

    # Check if the logged-in user is the one associated with the order
    if profile.user != request.user:
        messages.error(
            request, 'Sorry, you do not have permission to view this profile.')
        return redirect('home')


def profile(request):
    """Display the users profile information."""
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
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


def order_history(request, order_number):
    """Display the user's order information from their order history."""
    order = get_object_or_404(Order, order_number=order_number)

    # Check if the logged-in user is the one associated with the order
    if order.user_profile.user != request.user:
        messages.error(
            request, 'Sorry, you do not have permission to view this order.')
        return redirect('home')

    return render(request, 'checkout/checkout-success.html', {
        'order': order,
        'from_profile': True
    })


@login_required
def wishlist(request):
    """
    View function for displaying the user's wishlist.
    """
    wishlist_items = Wishlist.objects.filter(user_profile=request.user.profile)
    return render(request, 'profiles/wishlist.html', {
        'wishlist_items': wishlist_items
    })


@login_required
def toggle_wishlist_item(request):
    """
    Toggles a wishlist item for a user.
    """
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        profile = get_object_or_404(Profile, user=request.user)

        wishlist_item, created = Wishlist.objects.get_or_create(
            user_profile=profile, product=product)

        if created:
            action = 'added'
        else:
            wishlist_item.delete()
            action = 'removed'

        return JsonResponse({'status': 'ok', 'action': action})
    return JsonResponse({'status': 'error'}, status=400)
