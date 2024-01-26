# from django import forms
# from django.contrib.auth.models import User


# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Senha', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)
#     first_name = forms.CharField(label='Nome')
#     last_name = forms.CharField(label='Sobrenome')
#     email = forms.CharField(label='Email')
#     username = forms.CharField(label='Nome de usuário')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('As senhas não condizem')
#         return cd['password2']


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)
    
    TIPOS_USUARIO = [
        ('cliente', 'Cliente'),
        ('estabelecimento', 'Estabelecimento'),
    ]
    tipo_usuario = forms.ChoiceField(label='Tipo de Usuário', choices=TIPOS_USUARIO)

    class Meta:
        model = CustomUser
        fields = ('tipo_usuario', 'username', 'first_name', 'last_name', 'endereco', 'email', 'telefone', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('As senhas não condizem')
        return cd['password2']




