from django.urls import path
from rest_vehiculo.views import UserView

urlpatterns = [
    path('user', UserView.as_view())
]