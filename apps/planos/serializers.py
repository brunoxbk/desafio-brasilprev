from rest_framework import serializers
from apps.planos.models import Plano, Aporte, Resgate
from django.utils import timezone


class PlanoSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if not data['idProduto'].valido:
            raise serializers.ValidationError({"idProduto": "Produto com prazo expirado."})

        if data['idProduto'].valorMinimoAporteInicial >= data['aporte']:
            raise serializers.ValidationError({
                "idProduto": f"Valor mínimo de aporte no momento da contratação: {data['idProduto'].valorMinimoAporteInicial}"})

        if not data['idCliente'].idade >= data['idProduto'].idadeDeEntrada:
            raise serializers.ValidationError({"idCliente": f"Idade mínima para comprar o produto: {data['idProduto'].idadeDeEntrada}."})

        return data

    class Meta:
        model = Plano
        fields = [
            'id',
            'idCliente',
            'idProduto',
            'aporte',
            'dataDaContratacao',
            'idadeDeAposentadoria',
            'created',
            'updated'
        ]


class AporteSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if not data['idPlano'].idProduto.valido:
            raise serializers.ValidationError({"idProduto": "Produto com prazo expirado."})

        if not data['idPlano'].saldo > 0:
            raise serializers.ValidationError({"idPlano": "Plano sem saldo."})

        if data['idPlano'].idProduto.valorMinimoAporteExtra >= data['valorAporte']:
            raise serializers.ValidationError({
                "idProduto": f"Valor mínimo de aporte extra: {data['idPlano'].idProduto.valorMinimoAporteExtra}"})

        return data

    class Meta:
        model = Aporte
        fields = [
            'id',
            'idCliente',
            'idPlano',
            'valorAporte',
            'created',
            'updated'
        ]


class ResgateSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['valorResgate'] > data['idPlano'].saldo:
            raise serializers.ValidationError({
                "idProduto": f"Valor de saldo do plano: {data['idPlano'].saldo}"})

        if data['idPlano'].proximo_resgate > timezone.now():
            raise serializers.ValidationError({
                "idPlano": f"Data limite para o proximo resgate : {data['idPlano'].proximo_resgate.strftime('%Y-%m-%dT%H:%M')}"})

        return data

    class Meta:
        model = Resgate
        fields = [
            'id',
            'idPlano',
            'valorResgate',
            'created',
            'updated'
        ]