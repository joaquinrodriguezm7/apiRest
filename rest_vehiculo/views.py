from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UsuarioSerializer, VehiculoSerializer, ViajeSerializer
from core.models import Usuario, Vehiculo, Viaje
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
# Create your views here.

class UserView(APIView):
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
            nuevaPass = data['pass']

            usuario = Usuario.objects.get(nombre_usuario = usuario)

            usuario.password_usuario = nuevaPass
            usuario.save()
            return JsonResponse({'mensaje': 'La contraseña se ha modificado correctamente'})
        except Usuario.DoesNotExist:
            return  JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)
        
    def get(self, request):
        serializer = UsuarioSerializer(Usuario.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class VehiculoView(APIView):
    def get(self, request):
        serializer = VehiculoSerializer(Vehiculo.objects.all(), many=True)
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
    def get(self, request):
        serializer = ViajeSerializer(Viaje.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data,safe=False)
    
    def post(self,request):
        try:
            data = JSONParser().parse(request)
            Viaje.objects.create(
                inicio=data['inicio'],
                termino=data['termino'],
                costo=data['costo'],
                patente_id=data['patente'],
                nombre_usuario_dueño_id=data['nombre_usuario_dueño'],
            )
            return JsonResponse({"mensaje":"El Viaje se ha registrado exitosamente"}, status=200,safe=False) 
        except Exception as e:
            return JsonResponse(str(e), status=500)
        
