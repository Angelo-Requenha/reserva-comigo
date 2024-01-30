# urls.py
from django.contrib import admin
from django.urls import path, include
from .views import init_page, sobre_nos, init_page_usuario, home, pagina_convidativa

app_name = 'reserva_app'

urlpatterns = [
    path('', init_page, name='init_page'),
    path('sobre_nos/', sobre_nos, name='sobre_nos'),
    path('init_page_usuario/', init_page_usuario, name='init_page_usuario'),
    path('home', home, name='home'),
    path('pagina_convidativa', pagina_convidativa, name='pagina_convidativa'),
]
