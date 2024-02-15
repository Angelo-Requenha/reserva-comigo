from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import CustomUser 


# Create your views here.

@login_required
def grupos(request):
    return render(request, 'grupos.html')

@login_required
def feed(request):
    usuarios = CustomUser.objects.filter(tipo='E')
    context = {'usuarios': usuarios}
    return render(request, 'feed.html', context)

