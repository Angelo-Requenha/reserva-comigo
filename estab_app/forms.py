from django import forms
from .models import DataDisponibilidade

class FormularioData(forms.ModelForm):
    class Meta:
        model = DataDisponibilidade
        fields = ['data', 'disponivel']
        