from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel 

class Agendamento(BaseModel):
    prestador = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='agendamentos'
    )
    data_horario = models.DateTimeField()
    nome_cliente = models.CharField(max_length=255)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=20, blank=True, null=True)
    cancelado = models.BooleanField(default=False)

    class Meta:
       
        unique_together = ('prestador', 'data_horario')
        ordering = ['data_horario'] 

    def __str__(self):
        return f"{self.nome_cliente} com {self.prestador.username} em {self.data_horario.strftime('%d/%m/%Y %H:%M')}"