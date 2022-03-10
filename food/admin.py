
# Indiquation des model pour BDD

from django.contrib import admin
from .models import Order, FoodCategory, FoodItem, OrderItem
# Register your models here.


admin.site.register(Order)

admin.site.register(FoodCategory)

admin.site.register(FoodItem)

admin.site.register(OrderItem)
