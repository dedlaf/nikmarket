import django.contrib.admin
from django.contrib import admin
from .models import UserProfile, Order, Product, Cart, CartItem

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
