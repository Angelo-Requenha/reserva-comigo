from django import forms
from .models import Grupo

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'membros', 'estabelecimento', 'data_hora', 'duracao']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }