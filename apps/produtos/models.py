from django.db import models
import uuid
from django.utils import timezone


class Produto(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField("nome", max_length=120, blank=False, null=False)
    susep = models.CharField("susep", max_length=60, blank=False, null=False)
    expiracao_de_venda = models.DateTimeField("expiração de venda", blank=False, null=False)
    valor_minimo_aporte_inicial = models.DecimalField("valor minimo aporte inicial", decimal_places=2, max_digits=10)
    valor_minimo_aporte_extra = models.DecimalField("valor minimo aporte extra", decimal_places=2, max_digits=10)
    idade_de_entrada = models.IntegerField("idade entrada", blank=False, null=False)
    idade_de_saida = models.IntegerField("idade entrada", blank=False, null=False)
    carencia_inicial_de_resgate = models.IntegerField("carência inicial", blank=False, null=False)
    carencia_entre_resgates = models.IntegerField("carência entre resgates", blank=False, null=False)

    created = models.DateTimeField("criado", auto_now_add=True)
    updated = models.DateTimeField("alterado", auto_now=True)

    @property
    def valido(self):
        return timezone.now() < self.expiracao_de_venda

    def __str__(self):
        return f"{self.nome}"

