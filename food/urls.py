# Liens des pages

from django.urls import path

from . import views

app_name = 'food'

urlpatterns = [
     path('category/<int:category_id>', views.category, name='category'),
     path('order', views.order, name='order'),
     path('success', views.success, name='success'),
     path('signup', views.signup, name='signup'),
     path('login', views.logIn, name='login'),
     path('logout', views.logOut, name='logout'),
]