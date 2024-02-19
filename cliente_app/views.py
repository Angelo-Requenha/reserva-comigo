from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import CustomUser 
from .forms import GrupoForm


# Create your views here.

@login_required
def grupos(request):
    return render(request, 'grupos.html')

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
        return redirect('cliente_app:grupos.html')

    else:
        form = GrupoForm()

    return render(request, 'criar_grupo.html', {'form': form})