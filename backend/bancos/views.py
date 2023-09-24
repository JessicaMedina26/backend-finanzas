from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import Ciudad, Cliente, CuentaBancaria, Movimiento, Operacion
from .serializer import (ClienteSerializer, CiudadSerializer, CuentaBancariaSerializer,
                         OperacionSerializer, MovimientoSerializer)

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer(queryset, many=True)


    def list(self, request):
        queryset = Ciudad.objects.all()
        serializer_class = CiudadSerializer(queryset, many= True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


    def create(self, request):
        item = CiudadSerializer(data=request.data)
        if item.is_valid():
            item.save()
            return Response(item.data, status = status.HTTP_200_OK)
        return Response(item.errors, status = status.HTTP_400_BAD_REQUEST)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CuentaBancariaViewSet(viewsets.ModelViewSet):
    queryset = CuentaBancaria.objects.all()
    serializer_class = CuentaBancariaSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer

class OperacionViewSet(viewsets.ModelViewSet):
    queryset = Operacion.objects.all()
    serializer_class = OperacionSerializer
