from rest_framework import serializers
from apps.produtos.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'nome',
            'susep',
            'expiracaoDeVenda',
            'valorMinimoAporteExtra',
            'rendaMensal',
            'idadeDeEntrada',
            'idadeDeSaida',
            'carenciaInicialDeResgate',
            'carenciaEntreResgates'
        ]

