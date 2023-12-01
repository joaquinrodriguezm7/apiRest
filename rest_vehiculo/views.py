from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UsuarioSerializer, VehiculoSerializer
from core.models import Usuario, Vehiculo
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
                id_usuario=data['id_usuario']
            )
            return JsonResponse({"mensaje":"El Vehiculo se ha registrado exitosamente"}, status=200) 
        except Exception as e:
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)