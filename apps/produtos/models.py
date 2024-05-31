from django.db import models
import uuid


class Produto(models.Model):

    # "nome": "Brasilprev Longo Prazo",
    # "susep": "15414900840201817",
    # "expiracaoDeVenda": "2021-01-01T12:00:00.000Z",
    # "valorMinimoAporteInicial": 1000.0, // valor mínimo de aporte no momento da contratação
    # "valorMinimoAporteExtra": 100.0, // valor mínimo do aporte extra
    # "idadeDeEntrada": 18, // idade mínima para comprar o produto
    # "idadeDeSaida": 60, // idade máxima para começar a usufruir do benefício
    # "carenciaInicialDeResgate": 60, // em dias - carência para realizar o primeiro resgate
    # "carenciaEntreResgates": 30 // em dias - carência para realizar outro resgate após um resgate realizado.

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField("nome", max_length=120, blank=False, null=False)
    susep = models.CharField("susep", max_length=60, blank=False, null=False)
    expiracaoDeVenda = models.DateTimeField("expiração de venda", blank=False, null=False)
    valorMinimoAporteInicial = models.DecimalField("valor minimo aporte inicial", decimal_places=2, max_digits=10)
    valorMinimoAporteExtra = models.DecimalField("valor minimo aporte extra", decimal_places=2, max_digits=10)
    idadeDeEntrada = models.IntegerField("idade entrada", blank=False, null=False)
    idadeDeSaida = models.IntegerField("idade entrada", blank=False, null=False)
    carenciaInicialDeResgate = models.IntegerField("carência inicial", blank=False, null=False)
    carenciaEntreResgates = models.IntegerField("carência entre resgates", blank=False, null=False)

    created = models.DateTimeField("criado", auto_now_add=True)
    updated = models.DateTimeField("alterado", auto_now=True)

    def __str__(self):
        return f"{self.nome}"
