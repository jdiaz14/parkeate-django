from django.urls import path

from proyectowebapp import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('reservar', views.reservar, name="reservar"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('contacto', views.contacto, name="contacto"),
]