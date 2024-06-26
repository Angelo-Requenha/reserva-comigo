from django.db import models
from users.models import CustomUser


STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('recusado', 'Recusado'),
    ]

STATUS_PAGAMENTO_CHOICES = [
        ('pendente', 'Pendente'),
        ('Pago', 'Pago'),
    ]

class Grupo(models.Model):
    nome = models.CharField(verbose_name= 'Nome do grupo', max_length=255)
    membros = models.ManyToManyField(CustomUser, through='StatusPagamentoMembro')
    estabelecimento = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='grupos')
    ano = models.IntegerField(default = 2024)
    mes = models.IntegerField(default = 2)
    dia = models.IntegerField(default = 29)
    duracao = models.IntegerField(default = 0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return self.nome


class Notificacao(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mensagem = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')


class StatusPagamentoMembro(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    membro = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status_pagamento = models.CharField(max_length=20, choices=STATUS_PAGAMENTO_CHOICES, default='pendente')

    def __str__(self):
        return f"{self.membro.username} - {self.status_pagamento}"
