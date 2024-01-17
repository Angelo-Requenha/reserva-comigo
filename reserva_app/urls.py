# urls.py
from django.contrib import admin
from django.urls import path, include
from .views import init_page, cadastro, login, sobre_nos

app_name = 'reserva_app'

urlpatterns = [
    path('', cadastro, name='cadastro'),
    path('login/', login, name='login'),  # Certifique-se de que o caminho tenha uma barra final
    path('init_page/', init_page, name='init_page'),
    path('sobre_nos/class', sobre_nos, name='sobre_nos')
]
