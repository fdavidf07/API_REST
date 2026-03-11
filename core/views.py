from rest_framework import viewsets, permissions
from .models import Espacio, Reserva
from .serializers import EspacioSerializer, ReservaSerializer

class EspacioViewSet(viewsets.ModelViewSet):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer
    # SOLO EL ADMIN puede crear/borrar salas. El resto solo mira (GET).
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    # CUALQUIER LOGUEADO (como Ejemplo) puede reservar.
    permission_classes = [permissions.IsAuthenticated]