from django.shortcuts import render, redirect
from users.models import CustomUser 
from .models import DiaMarcado
from .forms import DiaForm, MesForm, AnoForm
import calendar
from django.urls import reverse

# Create your views here.

def generate_calendar(year, month):
    cal = calendar.HTMLCalendar().formatmonth(int(year), int(month))
    highlighted_days = []
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        if DiaMarcado.objects.filter(ano=year, mes=month, dia=day).exists():
            highlighted_days.append(str(day))
    for day in highlighted_days:
        highlighted_day = f'<span><strong>{day}</strong></span>'
        cal = cal.replace(f'>{day}<', f'>{highlighted_day}<')
    return cal

def pagina_estab(request, info_especifica):
    year = int(request.GET.get('year', 2024))
    month = int(request.GET.get('month', 2))
    calendar_html = generate_calendar(year, month)

    info = CustomUser.objects.filter(id=info_especifica)
    
    context = {
        'info': info,
        'year': year,
        'month': month,
        'calendar_html': calendar_html,
        }
    
    return render(request, 'pagina_estab.html', context)

def salvar(request):
    if request.method == 'POST':
        year = int(request.POST['year'])
        month = int(request.POST['month'])
        day = int(request.POST['day'])
        
        if DiaMarcado.objects.filter(ano=year, mes=month, dia=day).exists():
            
            context = {
                'year': year,
                'month': month,
                'calendar_html': generate_calendar(year, month),
                'error_message': 'Este dia já está marcado no calendário!'
            }
            
            return render(request, 'profile.html', context)
        
        DiaMarcado.objects.create(ano=year, mes=month, dia=day)
        return redirect(reverse('estab_app:profile'))



