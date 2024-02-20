from django.db import models
from users.models import CustomUser


class Grupo(models.Model):
    nome = models.CharField(verbose_name= 'Nome do grupo', max_length=255)
    membros = models.ManyToManyField(CustomUser)
    estabelecimento = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='grupos')
    ano = models.IntegerField()
    mes = models.IntegerField()
    dia = models.IntegerField()
    duracao = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.nome