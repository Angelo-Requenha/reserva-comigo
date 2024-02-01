from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ClienteForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'telefone', 'password1', 'password2']
        labels = {
            'email': 'Email',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'telefone': 'Telefone',
            'password1': 'Senha',
            'password2': 'Confirme a senha',
        }
        widgets = {
            'tipo': forms.HiddenInput(attrs={'value': 'C'}),
        }

class EstabelecimentoForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'endereco', 'telefone', 'password1', 'password2']
        labels = {
            'email': 'Email',
            'first_name': 'Nome do estabelecimento',
            'endereco': 'Endereço',
            'telefone': 'Telefone',
            'password1': 'Senha',
            'password2': 'Confirme a senha',
        }
        widgets = {
            'tipo': forms.HiddenInput(attrs={'value': 'E'}),
        }

