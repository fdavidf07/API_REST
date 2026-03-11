from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import EspacioViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'espacios', EspacioViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # AÑADE ESTA LÍNEA AQUÍ ABAJO:
    path('api-auth/', include('rest_framework.urls')), 
]