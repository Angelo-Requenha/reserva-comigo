from django import forms
from .models import Grupo
from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q

CustomUser = get_user_model()

class GrupoForm(forms.ModelForm):
    membros = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.filter(tipo='C'),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        label='Membros'
    )

    membros.widget.attrs.update({'data-placeholder': 'Selecione os membros', 'data-allow-clear': 'true'})

    class Meta:
        model = Grupo
        fields = ['nome', 'membros', 'ano', 'mes', 'dia', 'duracao']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['membros'].queryset = CustomUser.objects.filter(tipo='C')

    def clean_membros(self):
        membros = self.cleaned_data['membros']
        if not membros:
            raise forms.ValidationError('Selecione pelo menos um membro.')
        return membros
