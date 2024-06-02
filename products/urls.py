from django.urls import path
from . import views

urlpatterns = [
    path('<department>', views.products_list, name='products-list'),
]
