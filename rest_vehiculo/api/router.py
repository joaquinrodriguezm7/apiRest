from django.urls import path
from rest_vehiculo.views import UserView, VehiculoView, ViajeView, SedeView

urlpatterns = [
    path('user', UserView.as_view()),
    path('vehiculo', VehiculoView.as_view()),
    path('vehiculo/<str:nombre_usuario>/', VehiculoView.as_view()),
    path('viaje', ViajeView.as_view()),
    path('viaje/<int:id_viaje>/', ViajeView.as_view()),
    path('viaje/enviar-correo/', ViajeView.as_view(), name='enviar_correo_confirmacion'),
    path('sede', SedeView.as_view()),
]