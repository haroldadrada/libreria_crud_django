from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Bienvenidos a la librería</h1>")

def nosotros(request):
    return render(request, 'libreria/nosotros.html')

def libros(request):
    return render(request, 'libreria/index.html')