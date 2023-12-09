from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UsuarioSerializer, VehiculoSerializer, ViajeSerializer, SedeSerializar
from core.models import Usuario, Vehiculo, Viaje, Sede
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.parsers import JSONParser
from rest_framework.generics import get_object_or_404
from django.http import JsonResponse
# Create your views here.

class UserView(APIView):
    def get(self, request):
        serializer = UsuarioSerializer(Usuario.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            usuario = data['usuario']
            password = data['pass']
            serializer = UsuarioSerializer(Usuario.objects.get(nombre_usuario=usuario, password_usuario=password))
            return JsonResponse(serializer.data)
        except Usuario.DoesNotExist:
            return JsonResponse(status=400)
        except Exception as e:
            return JsonResponse(status=500)
    def put(self, request):
        try:
            data = JSONParser().parse(request)
            usuario = data['usuario']
            nuevaPass = data['password1']

            usuario = Usuario.objects.get(nombre_usuario = usuario)

            usuario.password_usuario = nuevaPass
            usuario.save()
            return JsonResponse({'mensaje': 'La contraseña se ha modificado correctamente'})
        except Usuario.DoesNotExist:
            return  JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)
    
class VehiculoView(APIView):
    def get(self, request, nombre_usuario=None):
        if nombre_usuario is not None:
            print("Nombre de usuario recibido:", nombre_usuario)
            vehiculos = Vehiculo.objects.filter(nombre_usuario__nombre_usuario=nombre_usuario)
        else:
            vehiculos = Vehiculo.objects.all()

        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self,request):
        try:
            data = JSONParser().parse(request)
            Vehiculo.objects.create(
                patente=data['patente'],
                marca=data['marca'],
                modelo=data['modelo'],
                capacidad=data['capacidad'],
                nombre_usuario_id=data['nombre_usuario'],
            )
            return JsonResponse({"mensaje":"El Vehiculo se ha registrado exitosamente"}, status=200) 
        except Exception as e:
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)
        
class ViajeView(APIView):
    def get(self, request, id_viaje=None):
        sede = self.request.query_params.get('sede', None)
        if sede:
            viajes = Viaje.objects.filter(nombre_sede__nombre_sede=sede)
            serializer = ViajeSerializer(viajes, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        elif id_viaje is not None:
            viaje = get_object_or_404(Viaje, id_viaje=id_viaje)
            serializer = ViajeSerializer(viaje)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            serializer = ViajeSerializer(Viaje.objects.all(), many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def detalleViaje(self, request, id_viaje):
        viaje = get_object_or_404(Viaje, id_viaje=id_viaje)
        serializer = ViajeSerializer(viaje)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        try:
            data = JSONParser().parse(request)

            Viaje.objects.create(
                nombre_sede_id=data['sede'],
                inicio=data['inicio'],
                termino=data['termino'],
                costo=data['costo'],
                patente_id=data['patente'],
                nombre_usuario_duenno_id=data['nombre_usuario_dueño'],
                capacidad_disponible=data['capacidad'],
            )

            return JsonResponse({"mensaje": "El Viaje se ha registrado exitosamente"}, status=200)
        except Exception as e:
            print(f'Error en la vista: {repr(e)}')
            return JsonResponse(str(e), status=500, safe=False)
        
    def put(self, request):
        try:
            data = JSONParser().parse(request)
            id_viaje = data['id_viaje']
            nombre_usuario_cliente_nombre = data['nombre_usuario_cliente']  # Cambiado el nombre para mayor claridad

            viaje = Viaje.objects.get(id_viaje=id_viaje)

            if viaje.capacidad_disponible > 0:
                # Buscar el objeto Usuario correspondiente al nombre de usuario
                usuario_cliente = Usuario.objects.get(nombre_usuario=nombre_usuario_cliente_nombre)

                viaje.nombre_usuario_cliente.add(usuario_cliente)
                viaje.capacidad_disponible -= 1
                viaje.save()

                return JsonResponse({'mensaje': 'Has tomado el viaje correctamente'}, status=200)
            else:
                return JsonResponse({'error': 'No hay capacidad disponible en el vehículo'}, status=400)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        except Exception as e:
            print(f'Error en la vista: {repr(e)}')
            return JsonResponse(str(e), status=500, safe=False)
    
class SedeView(APIView): 
    def get(self, request):
        serializer = SedeSerializar(Sede.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)