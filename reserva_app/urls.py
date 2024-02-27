# urls.py
from django.contrib import admin
from django.urls import path, include
from .views import sobre_nos, registro_c_e, pagina_convidativa

app_name = 'reserva_app'

urlpatterns = [
    path('sobre_nos/', sobre_nos, name='sobre_nos'),
    path('registro_c_e/', registro_c_e, name='registro_c_e'),
    path('', pagina_convidativa, name='pagina_convidativa'),
]
