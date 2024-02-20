from django.shortcuts import render
from users.models import CustomUser 


# Create your views here.

def pagina_estab(request, info_especifica):
    info = CustomUser.objects.filter(id=info_especifica)
    print(info)
    
    context = {
        'info': info,
        'user': request.user
    }
    
    template_name = "pagina_estab_cliente.html" if request.user.tipo == 'C' else "pagina_estab_estab.html"
    return render(request, template_name, context)

