from rest_framework import serializers
from .models import Agendamento
from django.utils import timezone

class AgendamentoSerializer(serializers.ModelSerializer):
    prestador_username = serializers.ReadOnlyField(source='prestador.username')

    class Meta:
        model = Agendamento
        fields = [
            'id',
            'data_horario',
            'nome_cliente',
            'email_cliente',
            'telefone_cliente',
            'prestador_username', 
            'cancelado',
        ]
        read_only_fields = ['cancelado'] 
    def validate_data_horario(self, value):
        """Validação customizada para o campo data_horario."""
        if value < timezone.now():
            raise serializers.ValidationError("Não é possível realizar um agendamento no passado.")
        return value