from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import FoodItemSerializer, OrderSerializer, OrderItemSerializer
import random
import json
import os



def randomOrderNumber(length):
    sample  = 'ABCDEFGH0123456789'
    number0 = ''.join((random.choice(sample) for i in range (length)))
    return number0

# Create your views here.

def index(request):
    request.session.set_expiry(0)
    ctx = {'categories': FoodCategory.objects.all(), 'active_link' : 'index' }
    return render(request, 'food/index.html', ctx)

def item(request):
    request.session.set_expiry(0)
    item = OrderItem.objects.all()
    ctx = {'item': FoodCategory.objects.all(), 'active_link' : 'item' }
    print(item)
    return render(request,'food/category.html', ctx ) 


def category(request, category_id):
    category = FoodCategory.objects.filter(id=category_id)
    category_name = 'Error' if not category else category[0].name
    food_items = FoodItem.objects.filter(food_category__id=category_id)
    for food_item in food_items:
        food_item.image = os.path.basename(food_item.image.url)
    ctx = {'categories': FoodCategory.objects.all(), 'items': food_items, 'category_name': category_name}
    return render(request, 'food/category.html', ctx)


@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
        orders = json.loads(request.session['order'])
        request.session['bill'] = request.POST.get('bill')
        randomNum = randomOrderNumber(6)

        while Order.objects.filter(number=randomNum).count() > 0:
            randomNum=randomOrderNumber(6)

        if request.user.is_authenticated:
            order = Order(customer=request.user,
                          number=randomNum,
                          bill=float(request.session['bill']), 
                          note=request.session['note'])
            order.save()
            request.session['orderNum'] = order.number
            for article in orders:
                item = OrderItem(
                    order=order,
                    food_item = FoodItem.objects.filter(id=int(article[3]))[0],
                    size_large = article[1] == 'L',
                )
                item.save()

    ctx = {'categories': FoodCategory.objects.all(), 'active_link' : 'order' }
    return render(request, 'food/order.html', ctx)

def success(request):
    orderNum = request.session['orderNum']
    bill = request.session['bill']
    items = OrderItem.objects.filter(order__number=orderNum)
    ctx = {'categories': FoodCategory.objects.all(), 'orderNum' : orderNum, 'bill' : bill, 'items' : items }
    return render(request,'food/success.html', ctx )

def signup(request):
    ctx = {'categories': FoodCategory.objects.all()}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        else:
            ctx['form'] = form
    else:
        form = NewUserForm()
        ctx['form'] = form
    return render(request, 'food/signup.html', ctx)

def logIn(request):
    if request.POST:
        username =  request.POST.get('username')
        pwd =  request.POST.get('password')
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Les champs sont incorects')
    ctx = {'categories': FoodCategory.objects.all(), 'active_link': 'login'}
    return render(request, 'food/login.html', ctx)

def logOut(request):
    logout(request)
    return redirect('index')



#Rest django framework 


class FoodItemViewSet(viewsets.ModelViewSet):

    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = (IsAuthenticated, )

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )

class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated, )





        