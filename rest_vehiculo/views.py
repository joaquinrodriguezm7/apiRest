from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.view.decorators.csrf import csrf_exempt
from core.models import Vehiculo
from .serializers import VehiculoSerializer
# Create your views here.
