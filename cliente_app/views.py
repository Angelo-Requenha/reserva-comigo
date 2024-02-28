from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import CustomUser, UserProfile
from .models import Grupo, Notificacao, StatusPagamentoMembro
from estab_app.models import DiaMarcado
from .forms import GrupoForm
from users.forms import ClienteProfileForm
import folium


# Create your views here.

@login_required
def grupos(request):
    todos_os_grupos = Grupo.objects.all()
    grupos_do_usuario = []

    for grupo in todos_os_grupos:
        if grupo.membros.filter(id=request.user.id).exists():
            grupos_do_usuario.append(grupo)
            print(grupos_do_usuario)
    
    context = {'grupos_lista': grupos_do_usuario}
    return render(request, 'grupos.html', context)

def grupo_infos(request, info_especifica, grupo_id):
    info = Grupo.objects.filter(id=grupo_id)
    
    grupo = Grupo.objects.get(id=grupo_id)
    valor_por_membro = grupo.duracao * grupo.estabelecimento.userprofile.valor_aluguel / grupo.membros.count()
    user_id = request.user.id

    if request.method == 'POST':
        pagamento = get_object_or_404(StatusPagamentoMembro, membro = user_id, grupo=grupo)
        pagamento.status_pagamento = 'pago'
        pagamento.save()
        return redirect('cliente_app:grupo_infos', info_especifica=info_especifica, grupo_id=grupo_id)

    lat, lon = UserProfile.objects.filter(email_id=info_especifica).values_list('latitude', flat=True).first(), UserProfile.objects.filter(email_id=info_especifica).values_list('longitude', flat=True).first()

    
    print()

    mapa = folium.Map(location=[lat, lon], zoom_start=12, width='50%', height='50%')

    folium.Marker([lat, lon], popup='Florianópolis').add_to(mapa)
    
    context = {
        'info': info,
        'mapa': mapa._repr_html_(),
        'valor_membro':valor_por_membro,
    }
    
    return render(request, 'grupo_infos.html', context)

@login_required
def feed(request):
    usuarios = CustomUser.objects.filter(tipo='E')
    
    context = {
        'usuarios': usuarios,
        
        }
    return render(request, 'feed.html', context)

def criar_grupo(request, info_especifica):
    info_estabelecimento = CustomUser.objects.get(id=info_especifica)

    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)

            year = grupo.ano 
            month = grupo.mes
            day = grupo.dia
            email = info_estabelecimento.email

            if DiaMarcado.objects.filter(ano=year, mes=month, dia=day, email_usuario=email).exists():   
                mensagem = 'Este dia já está marcado no calendário!'
                return render(request, 'criar_grupo.html', {'form': form, 'mensagem':mensagem})
            
            else:
                grupo.estabelecimento = info_estabelecimento
                grupo.save()
                        
                Notificacao.objects.create(
                    grupo=grupo,
                    estabelecimento=info_estabelecimento,
                    mensagem='Pedido de reserva pendente',
                )

                membros = form.cleaned_data['membros']
                grupo.membros.set(membros)
                grupo.save()  
            return redirect('/cliente/grupos/')

    else:
        form = GrupoForm()

    return render(request, 'criar_grupo.html', {'form': form, 'info': info_estabelecimento})

def profile_edit(request):
    user = request.user  
    if request.method == 'POST':
        form = ClienteProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/cliente/profile_edit/')  
    else:
        form = ClienteProfileForm(instance=user)

    return render(request, 'profile_edit.html', {'form': form})
