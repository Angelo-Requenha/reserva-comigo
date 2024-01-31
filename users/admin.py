from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Estabelecimento

class EstabelecimentoAdmin(UserAdmin):
    # Configurações específicas para o modelo Estabelecimento no Django Admin
    pass


admin.site.register(Estabelecimento, EstabelecimentoAdmin)
