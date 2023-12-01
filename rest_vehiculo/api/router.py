from django.urls import path
from rest_vehiculo.views import UserView, VehiculoView

urlpatterns = [
    path('user', UserView.as_view()),
    path('vehiculo', VehiculoView.as_view())
]