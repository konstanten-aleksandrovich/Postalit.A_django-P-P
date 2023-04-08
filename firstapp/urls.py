from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('products/',products,name='products'),
    path('products/<int:ptoductid>/',products,name='productsid'),
    path('users/',users,name='users'),
    path('users/<int:id>/<name>/',users,name='user'),
]
