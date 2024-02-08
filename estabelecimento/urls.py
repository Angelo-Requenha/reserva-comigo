# urls.py
from django.contrib import admin
from django.urls import path, include
from .views import init_page, cadastro, login, sobre_nos, init_page_usuario

app_name = 'estabelecimento'

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('', init_page, name='init_page'),
    path('sobre_nos/', sobre_nos, name='sobre_nos'),
    path('init_page_usuario/', init_page_usuario, name='init_page_usuario'),
]