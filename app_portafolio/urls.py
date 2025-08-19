from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('experiencia/', views.experiencia_laboral, name='experiencia_laboral'),
    path('certificados/', views.certificados, name='certificados'),
    path('contacto/', views.contacto, name='contacto'),
]