from django.shortcuts import render
from users.models import CustomUser 
import calendar
from datetime import datetime
from .forms import DiaForm, MesForm, AnoForm

# Create your views here.

def pagina_estab(request, info_especifica):
    ano_atual = datetime.now().year
    mes_atual = datetime.now().month
    dia_atual = datetime.now().day

    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    html_calendar = cal.formatmonth(ano_atual, mes_atual,dia_atual)

    info = CustomUser.objects.filter(first_name=info_especifica)

    if request.method == 'POST':
        dia_form = DiaForm(request.POST)
        mes_form = MesForm(request.POST)
        ano_form = AnoForm(request.POST)

        if dia_form.is_valid() and mes_form.is_valid() and ano_form.is_valid():
            dia = dia_form.cleaned_data['dia']
            mes = mes_form.cleaned_data['mes']
            ano = ano_form.cleaned_data['ano']

            # Criando um objeto de calendário
            cal = calendar.HTMLCalendar(calendar.SUNDAY)

            # Gerando o calendário para o mês selecionado
            html_calendar = cal.formatmonth(ano, int(mes))

            # Adicionando IDs únicos para cada célula do calendário
            html_calendar = html_calendar.replace(f'<td class="day">', '<td class="day" id="day-{ano}">')

            # Renderizando o modelo com o calendário e os formulários
            return render(request, 'pagina_estab.html', {
                'info': info,
                'calendario': html_calendar,
                'dia_form': dia_form,
                'mes_form': mes_form,
                'ano_form': ano_form
            })
    else:
        # Se não houver dados enviados, exibir os formulários vazios
        dia_form = DiaForm()
        mes_form = MesForm()
        ano_form = AnoForm()
    
    context = {
        'info': info,
        'calendario': html_calendar,
        'dia_form': dia_form,
        'mes_form': mes_form,
        'ano_form': ano_form,
        }
    
    return render(request, 'pagina_estab.html', context)
