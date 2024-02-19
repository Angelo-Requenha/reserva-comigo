# calendario_app/forms.py
from django import forms

class DiaForm(forms.Form):
    dia = forms.IntegerField(label='Dia', min_value=1, max_value=31)

class MesForm(forms.Form):
    mes = forms.ChoiceField(label='Mês', choices=[
        (1, 'Janeiro'),
        (2, 'Fevereiro'),
        (3, 'Março'),
        (4, 'Abril'),
        (5, 'Maio'),
        (6, 'Junho'),
        (7, 'Julho'),
        (8, 'Agosto'),
        (9, 'Setembro'),
        (10, 'Outubro'),
        (11, 'Novembro'),
        (12, 'Dezembro'),
    ])

class AnoForm(forms.Form):
    ano = forms.IntegerField(label='Ano', min_value=2024, max_value=2050)
