from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart(request):
    """
    Retrieves the cart information and calculates
    the total, delivery cost, and grand total.
    """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item in cart:
        product_id = item['id']
        product = get_object_or_404(Product, pk=product_id)
        size = item['size']
        quantity = item['quantity']
        total += quantity * product.current_price
        product_count += quantity
        cart_items.append({
            'item_id': product_id,
            'product': product,
            'size': size,
            'quantity': quantity,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'unique_shoe_count': len(cart_items),
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
