from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import CustomUser  # Importe o seu mo
from .forms import GrupoForm, MembroGrupoForm, FriendshipRequestForm, FriendshipResponseForm
from .models import MembroGrupo, Grupo, Friendship

# Create your views here.

@login_required
def grupos(request):
    grupos = Grupo.objects.all()
    if request.method == 'POST':
        grupo_form = GrupoForm(request.POST)
        if grupo_form.is_valid():
            grupo = grupo_form.save(commit=False)
            grupo.criador = request.CustomUser
            grupo.save()
            return redirect('cliente_app:grupos')  # Redirecionar para a raiz do site
    else:
        grupo_form = GrupoForm()
    return render(request, 'grupos.html', {'grupo_form': grupo_form, 'grupos': grupos})

@login_required
def adicionar_membro(request, grupo_id):
    grupo = Grupo.objects.get(id=grupo_id)
    if request.method == 'POST':
        membro_form = MembroGrupoForm(request.POST)
        if membro_form.is_valid():
            usuario = membro_form.cleaned_data['usuario']
            MembroGrupo.objects.create(grupo=grupo, usuario=usuario)
            return redirect('detalhes_grupo', grupo_id=grupo_id)  # Redirecionar para os detalhes do grupo após adicionar um membro
    else:
        membro_form = MembroGrupoForm()
    
    return render(request, 'adicionar_membro.html', {'membro_form': membro_form})

def feed(request):
    return render(request, 'feed.html')


@login_required
def send_friend_request(request, to_user_id):
    if request.method == 'POST':
        form = FriendshipRequestForm(request.POST)
        if form.is_valid():
            friendship_request = form.save(commit=False)
            friendship_request.from_user = request.user
            friendship_request.to_user_id = to_user_id
            friendship_request.save()
            return redirect('profile_view', user_id=to_user_id)
    else:
        form = FriendshipRequestForm()
    return render(request, 'friendship/send_friend_request.html', {'form': form})

@login_required
def respond_to_friend_request(request, friendship_request_id):
    friendship_request = Friendship.objects.get(pk=friendship_request_id)
    if request.method == 'POST':
        form = FriendshipResponseForm(request.POST, instance=friendship_request)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FriendshipResponseForm(instance=friendship_request)
    return render(request, 'friendship/respond_to_friend_request.html', {'form': form})
