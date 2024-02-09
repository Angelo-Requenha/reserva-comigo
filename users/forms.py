from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class ClienteForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        self.fields['password1'].widget.attrs['title'] = 'Sua senha precisa conter pelo menos 8 caracteres. Sua senha não pode ser uma senha comumente utilizada. Sua senha não pode ser inteiramente numérica.'
        self.fields['password2'].widget.attrs['title'] = 'Informe a mesma senha informada anteriormente, para verificação.'

    class Meta:
        model = CustomUser
        fields = ['foto_perfil', 'email', 'first_name', 'last_name', 'telefone', 'password1', 'password2']
        labels = {
            'foto_perfil': 'Foto de Perfil',
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
    def __init__(self, *args, **kwargs):
        super(EstabelecimentoForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        self.fields['password1'].widget.attrs['title'] = 'Sua senha precisa conter pelo menos 8 caracteres. Sua senha não pode ser uma senha comumente utilizada. Sua senha não pode ser inteiramente numérica.'
        self.fields['password2'].widget.attrs['title'] = 'Informe a mesma senha informada anteriormente, para verificação.'

    class Meta:
        model = CustomUser
        fields = ['foto_perfil', 'email', 'first_name', 'endereco', 'telefone', 'password1', 'password2']
        labels = {
            'foto_perfil': 'Foto de Perfil',
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


class CustomAuthenticationForm(AuthenticationForm):
    username_field = CustomUser._meta.get_field('email')
