from django.shortcuts import render
from users.models import CustomUser 


# Create your views here.

def pagina_estab(request, info_especifica):
    
    info = CustomUser.objects.filter(first_name=info_especifica)
    print(info)
    context = {
        'info': info
        }
    
    return render(request, 'pagina_estab.html', context)
