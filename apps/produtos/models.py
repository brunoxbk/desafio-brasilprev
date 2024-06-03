from django.db import models
import uuid
from django.utils import timezone

class Produto(models.Model):

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

    @property
    def valido(self):
        return timezone.now() < self.expiracaoDeVenda

    def __str__(self):
        return f"{self.nome}"

