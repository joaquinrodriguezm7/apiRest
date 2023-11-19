from rest_framework.views import APIView
from .serializers import UsuarioSerializer
from core.models import Usuario
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class UserView(APIView):
    def post(self, request):
        pass
        
    def get(self, request):
        serializer = UsuarioSerializer(Usuario.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)