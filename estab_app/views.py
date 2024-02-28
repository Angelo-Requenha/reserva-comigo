from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import CustomUser 
from .models import DiaMarcado
from cliente_app.models import Notificacao
import calendar
from django.urls import reverse

# Create your views here.

def generate_calendar(year, month, email):
    cal = calendar.HTMLCalendar().formatmonth(int(year), int(month))
    highlighted_days = []

    marked_days = DiaMarcado.objects.filter(ano=year, mes=month, email_usuario=email)

    for marked_day in marked_days:
        highlighted_days.append(marked_day.dia)
    
    for day in highlighted_days:
        highlighted_day = f'<span><strong>{day}</strong></span>'
        cal = cal.replace(f'>{day}<', f'>{highlighted_day}<')
        
    return cal


def pagina_estab(request, info_especifica):
    year = int(request.GET.get('year', 2024))
    month = int(request.GET.get('month', 2))

    info = CustomUser.objects.filter(id=info_especifica).first()

    if not info:
        return HttpResponse("CustomUser não encontrado com o ID fornecido.")

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

def calendario (request):
    user_email = request.user.email
    year = int(request.GET.get('year', 2024))
    month = int(request.GET.get('month', 2))
    calendar_html = generate_calendar(year, month, user_email)
    error_message = 'Data já cadastrada!'

    return render(request, 'estab_app/calendario.html', 
        {'year': year,
        'month': month,
        'calendar_html': calendar_html,})

@login_required
def salvar(request):
    if request.method == 'POST':
        year = int(request.POST['year'])
        month = int(request.POST['month'])
        day = int(request.POST['day'])
        
        user_email = request.user.email
        
        if DiaMarcado.objects.filter(ano=year, mes=month, dia=day, email_usuario=user_email).exists():
            context = {
                'year': year,
                'month': month,
                'calendar_html': generate_calendar(year, month, user_email),
                'error_message': 'Este dia já está marcado no calendário!'
            }
            
            return render(request, 'estab_app/profile.html', context)
        
        DiaMarcado.objects.create(ano=year, mes=month, dia=day, email_usuario=user_email)
        return redirect(reverse('estab_app:profile'))



def pedido_reserva(request, notificacao_id, acao):
    notificacao = get_object_or_404(Notificacao, id=notificacao_id)

    if request.user != notificacao.estabelecimento:
        return redirect('pagina_estab')  

    if notificacao.status == 'pendente':
        grupo = notificacao.grupo

        if acao == 'aceitar':
            grupo.status = 'confirmado'
            grupo.save()

            notificacao.status = 'confirmado'
            notificacao.save()

            year = grupo.ano
            month = grupo.mes
            day = grupo.dia
            email = request.user.email

            if DiaMarcado.objects.filter(ano=year, mes=month, dia=day, email_usuario=email).exists():
                mensagem = 'Você já tem uma reserva cadastrada para esta data!'
                return render (request, 'notificacoes.html', {'mensagem':mensagem})
            else:
                DiaMarcado.objects.create(ano=year, mes=month, dia=day, email_usuario=email)

        elif acao == 'recusar':
            grupo.delete()

    return redirect('/estab/notificacoes')

@login_required
def pagina_de_notificacoes(request):
    estabelecimento = get_object_or_404(CustomUser, id = request.user.id)
    notificacoes = Notificacao.objects.filter(estabelecimento=estabelecimento)
    

    return render(request, 'notificacoes.html', {'notificacoes': notificacoes})