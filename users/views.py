from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *

# Create your views here.


def register(request):
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


