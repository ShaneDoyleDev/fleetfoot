from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view-cart'),
    path('add-product/<product_id>',
         views.add_to_cart, name='add-to-cart'),
    path('update-cart/<product_id>',
         views.update_cart, name='update-cart'),
]
