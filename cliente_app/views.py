from django.shortcuts import render
import users.models

# Create your views here.

def grupos(request):
    
    return render(request, 'grupos.html')

def feed(request):
    return render(request, 'feed.html')
