from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel # Importando do nosso módulo core

class Perfil(BaseModel):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username