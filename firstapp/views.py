from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse('<h2>О саите</h2>')
def contact(request):
    return HttpResponse('<h2>Контакт</h2>')

def products(request,ptoductid=1):
    cat=request.GET.get('cat','NO')
    return  HttpResponse(f'<h2>Продукт № {ptoductid} Категория {cat}</h2>')
def users(request,id=0,name=''):
    id=request.GET.get('id','0')
    name=request.GET.get('name','No name')
    return  HttpResponse(f'<h2>Пользователь</h2><h3>id: {id}\nИмя: {name}</hЗ>')