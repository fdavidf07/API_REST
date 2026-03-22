from rest_framework import viewsets, permissions
from .models import Espacio, Reserva
from .serializers import EspacioSerializer, ReservaSerializer

# PERMISO PERSONALIZADO
class EsAdminOSoloLectura(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_staff or request.user.groups.filter(name='Admins_Espacios').exists()

class EspacioViewSet(viewsets.ModelViewSet):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer
    permission_classes = [EsAdminOSoloLectura]

class ReservaViewSet(viewsets.ModelViewSet):
    # El queryset base es obligatorio para evitar el AssertionError anterior
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Permitimos ver todas para que el cliente vea la disponibilidad
        return Reserva.objects.all()

    def perform_create(self, serializer):
        # Asigna el usuario que hace la petición automáticamente
        serializer.save(usuario=self.request.user)