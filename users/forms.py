from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Sobrenome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Nome de usuário', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('As senhas não condizem')
        return cd['password2']
  