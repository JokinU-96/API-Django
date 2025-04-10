from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from empresa.models import Departamento
from empresa.permissions import ReadOnlyPermission
from empresa.serialized import DepartamentoSerialized


# Create your views here.
class DepartamentoListView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]

    def get(self, request, *args, **kwargs):
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerialized(departamentos, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'nombre': request.data.get('nombre'),
            'telefono': request.data.get('telefono'),
        }
        serializer = DepartamentoSerialized(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartamentoDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]

    def get_object(self, departamento_id):
        try:
            return Departamento.objects.get(id=departamento_id)
        except Departamento.DoesNotExist:
            return None

    #Detalle del departamento.
    def get(self, request, departamento_id, *args, **kwargs):

        departamento_instance = self.get_object(departamento_id)

        if not (departamento_instance):
            return Response(
                {"res": "Object with departamento id does not exist"},
                status = status.HTTP_404_BAD_REQUEST
            )
        serializer = DepartamentoSerialized(departamento_instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    #Modificación del departamento.
    def put(self, request, departamento_id, *args, **kwargs):
        departamento_instance = self.get_object(departamento_id)
        if not departamento_instance:
            return Response(
                {"res": "Object with departamento id does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        data = {
            'nombre': request.data.get('nombre'),
            'telefono': request.data.get('telefono'),
        }
        serializer = DepartamentoSerialized(instance = departamento_instance, data = data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Borrar el departamento
    def delete(self, request, departamento_id, *args, **kwargs):
        departamento_instance = self.get_object(departamento_id)
        if not departamento_instance:
            return Response(
                {"res": "Object with departamento id does not exist"},
                status = status.HTTP_404_NOT_FOUND
            )
        departamento_instance.delete()
        return Response(
            {"res": "Object deleted"},
            status = status.HTTP_200_OK
        )