from django.shortcuts import render
from users.models import CustomUser 
import calendar

# Create your views here.

def pagina_estab(request, info_especifica):

    
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    
    # Gerando o calendário para o mês atual
    html_calendar = cal.formatmonth(2024, 10)
    
    info = CustomUser.objects.filter(first_name=info_especifica)
    print(info)
    context = {
        'info': info,
        'calendario': html_calendar,
        }
    
    return render(request, 'pagina_estab.html', context)
