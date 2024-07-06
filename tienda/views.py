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


def intex(request):
    context = {}
    return render(request, 'tienda.html',context)

def contacto(request):
    context = {}
    return render(request, 'contacto.html',context)

def nosotros(request):
    context = {}
    return render(request, 'nosotros.html',context)