from rest_framework import serializers
from core.models import Vehiculo
from core.models import Usuario
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca','modelo', 'categoria']
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'password']