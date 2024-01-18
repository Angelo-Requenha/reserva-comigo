from django.shortcuts import render, redirect
from .models import CustomUser


def cadastro(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        # Use create_superuser para criar um superusuário
        usuario = CustomUser.objects.create_user(email=email, password=senha)
        return redirect('reserva_app:login')  # Redirecione para a página de login após o registro bem-sucedido
    return render(request, 'register/cadastro.html')  # Renderize o formulário de registro

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            usuario = CustomUser.objects.get(email=email)
            if usuario.check_password(senha):
                # Lógica de sucesso de login
                return redirect('reserva_app:init_page_usuario')  # Redireciona para a página inicial após o login bem-sucedido
            else:
                # Lógica para lidar com senha incorreta
                return render(request, 'register/login.html', {'error_message': 'Senha incorreta. Tente novamente.'})
        except CustomUser.DoesNotExist:
            # Lógica para lidar com usuário inexistente
            return render(request, 'register/login.html', {'error_message': 'Usuário não encontrado. Tente novamente.'})
    return render(request, 'register/login.html')


def init_page(request):
    return render(request, 'pages/init_page.html')

def sobre_nos(request):
    return render(request, 'pages/sobre_nos.html')

def init_page_usuario(request):
    return render(request, 'pages/init_page_usuario.html')