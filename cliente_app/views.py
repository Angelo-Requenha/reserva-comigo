from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import CustomUser 
from .models import Grupo
from .forms import GrupoForm


# Create your views here.

@login_required
def grupos(request):
    grupos_lista = Grupo.objects.all()
    context = {'grupos_lista': grupos_lista}
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
            grupo.estabelecimento = info_estabelecimento
            grupo.save()
            membros = form.cleaned_data['membros']
            grupo.membros.set(membros)
            grupo.save()  # Salve novamente para garantir que as associações sejam salvas
        return redirect('/cliente/grupos/')

    else:
        form = GrupoForm()

    return render(request, 'criar_grupo.html', {'form': form, 'info': info_estabelecimento})
