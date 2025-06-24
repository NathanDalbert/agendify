from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Agendamento
from .serializers import AgendamentoSerializer 

class AgendamentoViewSet(viewsets.ModelViewSet):
    serializer_class = AgendamentoSerializer

    def get_queryset(self):
        """Filtra os agendamentos para retornar apenas os do usuário logado."""
        user = self.request.user

        return Agendamento.objects.filter(prestador=user, cancelado=False)

    def perform_create(self, serializer):
        """Associa o usuário logado como prestador ao criar um agendamento."""
        serializer.save(prestador=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """Muda a lógica de DELETE para um 'soft delete' (apenas cancela)."""
        agendamento = self.get_object()
        agendamento.cancelado = True
        agendamento.save()
        return Response(status=status.HTTP_204_NO_CONTENT)