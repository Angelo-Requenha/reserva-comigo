from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Estabelecimento(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group, related_name='estabelecimento_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='estabelecimento_user_permissions')


class Cliente(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='cliente_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='cliente_user_permissions')

