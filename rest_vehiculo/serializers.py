from rest_framework import serializers
from core.models import Usuario, Vehiculo, Viaje, Sede
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca','modelo','capacidad','nombre_usuario']
        safe = False
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nombre_usuario', 'password_usuario','tipoUsuario','correo_usuario']
        safe = False

class ViajeSerializer(serializers.ModelSerializer):
    # ... otros campos ...

    nombre_usuario_cliente = serializers.SerializerMethodField()

    def get_nombre_usuario_cliente(self, viaje):
        # Devuelve una lista de nombres de usuarios clientes asociados al viaje
        return [usuario.nombre_usuario for usuario in viaje.nombre_usuario_cliente.all()]

    class Meta:
        model = Viaje
        fields = '__all__'

class SedeSerializar(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'
        safe = False