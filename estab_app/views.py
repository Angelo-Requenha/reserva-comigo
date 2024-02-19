from django.shortcuts import render
from users.models import CustomUser 
from .models import DataDisponibilidade
import calendar

def schedule (request):
    return render(request, 'estab_app/schedule.html')

def pagina_estab(request, info_especifica):
    info = CustomUser.objects.filter(id=info_especifica)
    print(info)
    datas = DataDisponibilidade.objects.all()
    
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    
    # Gerando o calendário para o mês atual
    html_calendar = cal.formatmonth(2024, 10)
    
    info = CustomUser.objects.filter(first_name=info_especifica)
    print(info)
    context = {
        'info': info,
        'calendario': html_calendar,
        }
    
    context = {
        'info': info,
        'user': request.user
    }
    
    template_name = "pagina_estab_cliente.html" if request.user.tipo == 'C' else "pagina_estab_estab.html"
    return render(request, template_name, context)

