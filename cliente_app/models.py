# No arquivo models.py do seu aplicativo cliente_app

from django.conf import settings
from django.db import models

class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    criador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class MembroGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, related_name='membros', on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} - {self.grupo.nome}"

class Friendship(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friend_requests_received', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['from_user', 'to_user']
