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

    def clean(self):
        cleaned_data = super().clean()
        tipo_usuario = cleaned_data.get('tipo_usuario')

        if tipo_usuario == 'cliente':
            # Tornar campos específicos para cliente visíveis
            self.fields['first_name'].widget = forms.TextInput()
            self.fields['last_name'].widget = forms.TextInput()
            self.fields['endereco'].widget = forms.HiddenInput()
            self.fields['telefone'].widget = forms.HiddenInput()
        elif tipo_usuario == 'estabelecimento':
            # Tornar campos específicos para estabelecimento visíveis
            self.fields['first_name'].widget = forms.HiddenInput()
            self.fields['last_name'].widget = forms.TextInput()
            self.fields['endereco'].widget = forms.TextInput()
            self.fields['telefone'].widget = forms.TextInput()

        return cleaned_data


