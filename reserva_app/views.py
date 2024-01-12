from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.

def login(request):
    return render(request, 'register/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faça o login do usuário após o registro
            return redirect('/')  # Redirecione para a página de perfil após o registro
    else:
        form = CustomUserCreationForm()
        
    context = {
        'form': form
    }
    
    return render(request, 'registration/register.html', context)