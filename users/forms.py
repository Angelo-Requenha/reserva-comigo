from django import forms
from django.contrib.auth.models import User
from .models import Estabelecimento, Cliente
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.CharField(label='Email')
    username = forms.CharField(label='Nome de usuário')

    class Meta:
        model = Cliente
        fields = ('username', 'first_name', 'last_name', 'email', 'telefone')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('As senhas não condizem')
        return cd['password2']



class EstabRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nome do estabelecimento')
    endereco = forms.CharField(label='Endereço do seu estabelecimento')
    username = forms.CharField(label='Nome de usuário')

    class Meta:
        model = Estabelecimento
        fields = ('username', 'first_name', 'endereco', 'email', 'telefone', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('As senhas não condizem')
        return cd['password2']




