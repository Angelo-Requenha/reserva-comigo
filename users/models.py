from django.contrib.auth.models import AbstractUser
from django.db import models

class Estabelecimento(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255)