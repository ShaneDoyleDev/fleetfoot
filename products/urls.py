from django.urls import path
from . import views

urlpatterns = [
    path('department/<department>', views.products_list, name='products-list'),
    path('product-detail/<int:product_id>',
         views.product_detail, name='product-detail'),
    path('product-admin/', views.product_admin, name='product-admin'),
]
