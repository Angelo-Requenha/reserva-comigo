from django import forms
from django.contrib.auth.models import User
from .models import Estabelecimento
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.CharField(label='Email')
    username = forms.CharField(label='Nome de usuário')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('As senhas não condizem')
        return cd['password2']



class EstabRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nome do estabelecimento', widget=forms.PasswordInput)
    endereco = forms.CharField(label='Endereço do seu estabelecimento', widget=forms.PasswordInput)

    class Meta:
        model = Estabelecimento
        fields = ('first_name', 'endereco', 'email', 'telefone', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('As senhas não condizem')
        return cd['password2']
    

class CustomLoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = CustomUser.objects.filter(email=email).first()

            if user and user.check_password(password):
                self.user_cache = user
            else:
                raise forms.ValidationError('Por favor, insira um email e senha corretos.')

        return self.cleaned_data