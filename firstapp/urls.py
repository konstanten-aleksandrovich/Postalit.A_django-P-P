from django.urls import path
from .views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('',index,name='index'),
    path('about/',TemplateView.as_view(template_name='firstapp/about.html'),name='about'),
    path('contact/',TemplateView.as_view(template_name='firstapp/contact.html',extra_context={"work":
"Разработка программных продуктов"}),name='contact'),
    path('products/',products,name='products'),
    path('products/<int:ptoductid>/',products,name='productsid'),
    path('users/',users,name='users'),
    path('users/<int:id>/<name>/',users,name='user'),
]
