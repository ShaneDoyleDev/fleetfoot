from django.contrib import admin
from products.models import Product, ProductStock


admin.site.register(Product)
admin.site.register(ProductStock)
