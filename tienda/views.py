from django.shortcuts import render

# Create your views here.

def base(request):
    context = {}
    return render(request, 'base.html',context)


def intex(request):
    context = {}
    return render(request, 'tienda.html',context)

def contacto(request):
    context = {}
    return render(request, 'contacto.html',context)