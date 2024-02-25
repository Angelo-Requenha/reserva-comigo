from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def sobre_nos(request):
    return render(request, 'pages/sobre_nos.html')

def pagina_convidativa (request):
    return render(request, 'pages/pagina_convidativa.html')

def registro_c_e(request):
    return render(request, 'pages/registro_c_e.html')
