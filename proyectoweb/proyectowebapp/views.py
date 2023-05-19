from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render (request, "proyectowebapp/inicio.html")

def reservar(request):
    return render (request, "proyectowebapp/reservar.html")

def nosotros(request):
    return render (request, "proyectowebapp/nosotros.html")

def contacto(request):
    return render (request, "proyectowebapp/contacto.html")
