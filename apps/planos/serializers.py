from rest_framework import serializers
from apps.planos.models import Plano, Aporte, Resgate
from django.utils import timezone


class PlanoSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if not data['produto'].valido:
            raise serializers.ValidationError({"produto": "Produto com prazo expirado."})

        if data['produto'].valor_minimo_aporte_inicial >= data['aporte']:
            raise serializers.ValidationError({
                "produto": f"Valor mínimo de aporte no momento da contratação: {data['produto'].valor_minimo_aporte_inicial}"})

        if not data['cliente'].idade >= data['produto'].idade_de_entrada:
            raise serializers.ValidationError({"cliente": f"Idade mínima para comprar o produto: {data['produto'].idade_de_entrada}."})

        return data

    class Meta:
        model = Plano
        fields = [
            'id',
            'cliente',
            'produto',
            'aporte',
            'data_da_contratacao',
            'idade_de_aposentadoria',
            'created',
            'updated'
        ]

class AporteSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if not data['plano'].produto.valido:
            raise serializers.ValidationError({"produto": "Produto com prazo expirado."})

        if not data['plano'].saldo > 0:
            raise serializers.ValidationError({"plano": "Plano sem saldo."})

        if data['plano'].produto.valor_minimo_aporte_extra >= data['valor_aporte']:
            raise serializers.ValidationError({
                "produto": f"Valor mínimo de aporte extra: {data['plano'].produto.valor_minimo_aporte_extra}"})

        return data

    class Meta:
        model = Aporte
        fields = [
            'id',
            'cliente',
            'plano',
            'valor_aporte',
            'created',
            'updated'
        ]


class ResgateSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['valor_resgate'] > data['plano'].saldo:
            raise serializers.ValidationError({
                "produto": f"Valor de saldo do plano: {data['plano'].saldo}"})

        if data['plano'].proximo_resgate > timezone.now():
            raise serializers.ValidationError({
                "plano": f"Data limite para o próximo resgate : {data['plano'].proximo_resgate.strftime('%Y-%m-%dT%H:%M')}"})

        return data

    class Meta:
        model = Resgate
        fields = [
            'id',
            'plano',
            'valor_resgate',
            'created',
            'updated'
        ]