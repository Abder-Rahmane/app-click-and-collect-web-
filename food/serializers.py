from rest_framework import serializers

from .models import FoodItem, OrderItem, Order
from .forms import NewUserForm
from django.contrib.auth.models import User




 
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email')



class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodItem
        fields = ('name',)



class OrderItemSerializer(serializers.ModelSerializer):

    
    food_items = FoodItemSerializer(source='food_item')

    
    class Meta:
        model = OrderItem
        fields = ('size_large', 'food_items')   


class OrderSerializer(serializers.ModelSerializer):
    
    order_items = OrderItemSerializer(source="orderitem_set", many=True, read_only=True)
    user = UserSerializer(source="customer", many=False, read_only=True)
    

    class Meta:
        model = Order
        fields = ('user', 'number', 'bill', 'date', 'note', 'order_items')






