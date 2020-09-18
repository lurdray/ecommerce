from django.contrib import admin
from product.models import Product, ProductQuantity, Review

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductQuantity)
admin.site.register(Review)
