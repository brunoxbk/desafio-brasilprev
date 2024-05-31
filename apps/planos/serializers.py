from rest_framework import serializers
from apps.planos.models import Plano


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = [
            'idCliente',
            'idProduto',
            'aporte',
            'dataDaContratacao',
            'idadeDeAposentadoria',
            'created',
            'updated'
        ]