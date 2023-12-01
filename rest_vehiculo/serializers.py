from rest_framework import serializers
from core.models import Vehiculo
from core.models import Usuario
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca','modelo','capacidad']
        safe = False
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nombre_usuario', 'password_usuario','tipoUsuario']