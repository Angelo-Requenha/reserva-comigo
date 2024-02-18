from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, UserProfile, FotosEstab
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

	endereco = forms.CharField(max_length=100, widget = forms.HiddenInput())
	cep = forms.CharField(max_length=9, widget = forms.HiddenInput())
	pais = forms.CharField(max_length=40, widget = forms.HiddenInput())
	longitude = forms.CharField(max_length=50, widget = forms.HiddenInput())
	latitude = forms.CharField(max_length=50, widget = forms.HiddenInput())


	class Meta:
		model = UserProfile
		fields = ('endereco',  'cep',
		 'pais', 'longitude', 'latitude', 'valor_aluguel', 'capacidade_pessoas', 'tipo_horario')
          

class FotosEstabForm(forms.ModelForm):
    class Meta:
        model = FotosEstab
        fields = ['foto1', 'foto2', 'foto3', 'foto4', 'foto5', 'foto6']

    def clean(self):
        cleaned_data = super().clean()

        if not any(cleaned_data.get(foto) for foto in ['foto1', 'foto2', 'foto3', 'foto4', 'foto5', 'foto6']):
            raise forms.ValidationError('Pelo menos uma foto deve ser fornecida.')
        
