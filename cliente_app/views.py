from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from .models import Grupo, Notificacao
from estab_app.models import DiaMarcado
from .forms import GrupoForm




# Create your views here.

@login_required
def grupos(request):
    todos_os_grupos = Grupo.objects.all()
    grupos_do_usuario = []

    # Verifica se o usuário está entre os membros de cada grupo
    for grupo in todos_os_grupos:
        if grupo.membros.filter(id=request.user.id).exists():
            grupos_do_usuario.append(grupo)
            print(grupos_do_usuario)
    
    grupos_lista = Grupo.objects.all()
    context = {'grupos_lista': grupos_do_usuario}
    return render(request, 'grupos.html', context)

def grupo_infos(request, info_especifica):
    info = Grupo.objects.filter(id=info_especifica)
    context = {
        'info': info,
    }
    
    return render(request, 'grupo_infos.html', context)

@login_required
def feed(request):
    usuarios = CustomUser.objects.filter(tipo='E')
    context = {'usuarios': usuarios}
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
                grupo.save()  # Salve novamente para garantir que as associações sejam salvas
            return redirect('/cliente/grupos/')

    else:
        form = GrupoForm()

    return render(request, 'criar_grupo.html', {'form': form, 'info': info_estabelecimento})


