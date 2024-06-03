from rest_framework import serializers
from apps.clientes.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            "pk",
            "cpf",
            "nome",
            "email",
            "dataDeNascimento",
            'idade',
            "genero",
            "rendaMensal",
            "created",
            "updated"
        ]