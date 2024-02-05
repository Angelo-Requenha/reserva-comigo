from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


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

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

class CustomAuthenticationForm(AuthenticationForm):
    username_field = CustomUser._meta.get_field('email')
