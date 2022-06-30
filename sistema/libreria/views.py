from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'libreria/inicio.html')

def nosotros(request):
    return render(request, 'libreria/nosotros.html')

def libros(request):
    return render(request, 'libreria/index.html')