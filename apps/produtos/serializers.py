from rest_framework import serializers
from apps.produtos.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'pk',
            'nome',
            'susep',
            'expiracao_de_venda',
            'valor_minimo_aporte_inicial',
            'valor_minimo_aporte_extra',
            'idade_de_entrada',
            'idade_de_saida',
            'carencia_inicial_de_resgate',
            'carencia_entre_resgates'
        ]

