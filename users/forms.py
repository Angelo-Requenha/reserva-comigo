from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, UserProfile
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
        fields = ['foto_perfil', 'email', 'first_name', 'telefone', 'password1', 'password2']
        labels = {
            'foto_perfil': 'Foto de Perfil',
            'email': 'Email',
            'first_name': 'Nome do estabelecimento',
            'telefone': 'Telefone',
            'password1': 'Senha',
            'password2': 'Confirme a senha',
        }
        widgets = {
            'tipo': forms.HiddenInput(attrs={'value': 'E'}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    username_field = CustomUser._meta.get_field('email')


class UserProfileForm(forms.ModelForm):
	'''
	Basic model-form for our user profile that extends Django user model.
	
	'''
	address = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	town = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	county = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	post_code = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
	country = forms.CharField(max_length=40, required=True, widget = forms.HiddenInput())
	longitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())
	latitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())


	class Meta:
		model = UserProfile
		fields = ('address', 'town', 'county', 'post_code',
		 'country', 'longitude', 'latitude')