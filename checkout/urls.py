from django.urls import path
from . import views
from checkout.webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout-success/<order_number>',
         views.checkout_success, name='checkout-success'),
    path('cache-checkout-data/',
         views.cache_checkout_data, name='cache-checkout-data'),
    path('webhook/',
         webhook, name='webhook'),
]
