from rest_framework import serializers

from empresa.models import Departamento


class DepartamentoSerialized(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ["id", "nombre", "telefono", "created_at", "updated_at"]
