from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
# Create your views here.

def inicio(request):
    return render(request, 'libreria/inicio.html')

def nosotros(request):
    return render(request, 'libreria/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libreria/index.html', {'libros': libros})

def crear(request):
    return render(request, 'libreria/crear.html')

def editar(request):
    return render(request, 'libreria/editar.html')