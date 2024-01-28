from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        # Redireciona para a página desejada se o usuário já estiver autenticado
        return redirect('reserva_app:init_page')
    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Cria um novo objeto de usuário mas não salva ainda
            new_user = user_form.save(commit=False)
            # Define a senha escolhida
            new_user.set_password(user_form.cleaned_data['password1'])
            # Salva o objeto de usuário
            new_user.save()
            return render(request,'registration/register_done.html',{'new_user': new_user})
    else:        
        user_form = UserRegistrationForm()
        
    return render(request, 'registration/register.html', {'user_form': user_form})

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('reserva_app:init_page')
    
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('reserva_app:home')
    
    else:
        form = CustomLoginForm()
        
    return render(request, 'registration/login.html', {'form': form})