from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'inicio.html', context)

def productos(request):
    context = {}
    return render(request, 'tienda.html', context)

# Vista base para pruebas
def base(request):
    context = {}
    return render(request, 'base.html',context)