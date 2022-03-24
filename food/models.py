from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Model pour BDD
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    number   = models.CharField(max_length=60)
    bill     = models.DecimalField(max_digits=20, decimal_places=2)
    date     = models.DateTimeField(auto_now_add=True, blank=True)
    note     = models.TextField(blank=True, null=True)


class FoodCategory(models.Model):
    name = models.CharField(max_length=120)


class FoodItem(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='food/static/food/images')
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    priceM = models.DecimalField(max_digits=4, decimal_places=2)
    priceL = models.DecimalField(max_digits=4, decimal_places=2)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    size_large = models.BooleanField()


