from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import CustomUser 
from .models import DiaMarcado
import calendar
from django.urls import reverse

# Create your views here.

def generate_calendar(year, month, email):
    cal = calendar.HTMLCalendar().formatmonth(int(year), int(month))
    highlighted_days = []
    
    # Filtrando os dias marcados para o usuário com o email fornecido
    marked_days = DiaMarcado.objects.filter(ano=year, mes=month, email_usuario=email)
    
    # Adicionando os dias marcados à lista de dias destacados
    for marked_day in marked_days:
        highlighted_days.append(marked_day.dia)
    
    for day in highlighted_days:
        highlighted_day = f'<span><strong>{day}</strong></span>'
        cal = cal.replace(f'>{day}<', f'>{highlighted_day}<')
        
    return cal



def pagina_estab(request, info_especifica):
    year = int(request.GET.get('year', 2024))
    month = int(request.GET.get('month', 2))

    # Filtrando o CustomUser pelo id e obtendo o primeiro objeto do queryset
    info = CustomUser.objects.filter(id=info_especifica).first()
    
    if not info:
        # Tratar o caso em que nenhum CustomUser é encontrado com o id fornecido
        # Por exemplo, você pode retornar uma resposta de erro ou redirecionar para outra página
        return HttpResponse("CustomUser não encontrado com o ID fornecido.")

    # Verificando se info não é None antes de acessar seu atributo email
    calendar_html = generate_calendar(year, month, info.email if info else None)
    
    context = {
        'info': info,
        'year': year,
        'month': month,
        'calendar_html': calendar_html,
        'user': request.user
    }
    
    template_name = "pagina_estab_cliente.html" if request.user.tipo == 'C' else "pagina_estab_estab.html"
    return render(request, template_name, context)

@login_required
def salvar(request):
    if request.method == 'POST':
        year = int(request.POST['year'])
        month = int(request.POST['month'])
        day = int(request.POST['day'])
        
        # Obtendo o e-mail do usuário autenticado
        user_email = request.user.email
        
        if DiaMarcado.objects.filter(ano=year, mes=month, dia=day, email_usuario=user_email).exists():
            context = {
                'year': year,
                'month': month,
                'calendar_html': generate_calendar(year, month, user_email),
                'error_message': 'Este dia já está marcado no calendário!'
            }
            
            return render(request, 'profile.html', context)
        
        DiaMarcado.objects.create(ano=year, mes=month, dia=day, email_usuario=user_email)
        return redirect(reverse('estab_app:profile'))

