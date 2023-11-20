from rest_framework.views import APIView
from .serializers import UsuarioSerializer
from core.models import Usuario
from rest_framework.response import Response
from rest_framework import status
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
        

        
        
    def get(self, request):
        serializer = UsuarioSerializer(Usuario.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)