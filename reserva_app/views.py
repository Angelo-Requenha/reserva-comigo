from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.

def login(request):
    return render(request, 'register/login.html')


def init_page(request):
    return render(request, 'pages/init_page.html')