from django import forms
from .models import Grupo

class GrupoForm(forms.ModelForm):

    class Meta:
        model = Grupo
        fields = ['nome', 'membros', 'data_hora', 'duracao']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }

class DiaForm(forms.Form):
    dia = forms.IntegerField(label='Dia', min_value=1, max_value=31)