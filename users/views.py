from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import login


# Create your views here.


def register_cliente(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Cria um novo objeto de usuário mas não salva ainda
            new_user = user_form.save(commit=False)
            # Define a senha escolhida
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Salva o objeto de usuário
            new_user.save()
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:        
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register_cliente.html',
                  {'user_form': user_form})


def register_estab(request):
    if request.method == 'POST':
        estab_form = EstabRegistrationForm(request.POST)
        if estab_form.is_valid():
            new_estab = estab_form.save(commit=False)
            new_estab.set_password(estab_form.cleaned_data['password1'])
            new_estab.save()
            login(request, new_estab)
            return render(request, 'registration/register_done.html', {'new_user': new_estab})
    else:
        estab_form = EstabRegistrationForm()
    return render(request, 'registration/register_estab.html', {'estab_form': estab_form})