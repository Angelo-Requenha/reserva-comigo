from django.shortcuts import render, redirect
from .models import CustomUser

def init_page(request):
    return render(request, 'pages/init_page.html')

def sobre_nos(request):
    return render(request, 'pages/sobre_nos.html')

def init_page_usuario(request):
    return render(request, 'pages/init_page_usuario.html')

def home (request):
    return render(request, 'pages/home.html')