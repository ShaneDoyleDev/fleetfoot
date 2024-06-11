def wishlist_product_ids(request):
    if request.user.is_authenticated:
        ids = list(request.user.profile.wishlists.values_list(
            'product_id', flat=True))
        return {'wishlist_product_ids': ids}
    return {'wishlist_product_ids': []}
