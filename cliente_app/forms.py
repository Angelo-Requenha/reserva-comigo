# No seu arquivo forms.py do novo app
from django import forms
from users.models import CustomUser  # Importe o seu modelo CustomUser aqui
from .models import Grupo
from .models import Friendship


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'descricao']

# O formulário acima é para criar o grupo. Agora, precisamos de um formulário
# para adicionar membros ao grupo.

class MembroGrupoForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=CustomUser.objects.all())  # Usando CustomUser em vez de User


class FriendshipRequestForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = []

class FriendshipResponseForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = ['accepted']
