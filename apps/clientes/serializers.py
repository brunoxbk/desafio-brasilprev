from rest_framework import serializers
from products.models import Product


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "pk",
            "cpf",
            "nome",
            "email",
            "dataDeNascimento",
            "rendaMensal",
            "created",
            "updated"
        ]