from rest_framework import serializers
from apps.produtos.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'pk',
            'nome',
            'susep',
            'expiracaoDeVenda',
            'valorMinimoAporteInicial',
            'valorMinimoAporteExtra',
            'idadeDeEntrada',
            'idadeDeSaida',
            'carenciaInicialDeResgate',
            'carenciaEntreResgates'
        ]

