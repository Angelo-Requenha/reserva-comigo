from django.contrib.auth.backends import ModelBackend
from .models import Cliente, Estabelecimento

class CustomBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        cliente_user = Cliente.objects.filter(email__iexact=email).first()
        if cliente_user and cliente_user.check_password(password):
            return cliente_user

        estabelecimento_user = Estabelecimento.objects.filter(email__iexact=email).first()
        if estabelecimento_user and estabelecimento_user.check_password(password):
            return estabelecimento_user

        return None