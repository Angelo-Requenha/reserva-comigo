from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Estabelecimento, Cliente


admin.site.register(Estabelecimento)
admin.site.register(Cliente)