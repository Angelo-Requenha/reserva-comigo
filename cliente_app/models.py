from django.db import models
from users.models import CustomUser


class Grupo(models.Model):
    nome = models.CharField(verbose_name= 'Nome do grupo', max_length=255)
    membros = models.ManyToManyField(CustomUser)
    estabelecimento = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='grupos')
    ano = models.IntegerField(default = 2024)
    mes = models.IntegerField(default = 2)
    dia = models.IntegerField(default = 29)
    duracao = models.IntegerField(default = 0)

    def __str__(self):
        return self.nome