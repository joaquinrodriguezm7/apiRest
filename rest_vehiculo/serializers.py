from rest_framework import serializers
from core.models import Usuario, Vehiculo, Viaje
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca','modelo','capacidad','nombre_usuario']
        safe = False
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nombre_usuario', 'password_usuario','tipoUsuario']
        safe = False
class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'
        safe = False