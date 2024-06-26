from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order-history/<order_number>',
         views.order_history, name='order-history'),
    path('wishlist/',
         views.wishlist, name='wishlist'),
    path('toggle-wishlist-item/',
         views.toggle_wishlist_item, name='toggle-wishlist-item'),
]
