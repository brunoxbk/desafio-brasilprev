from django.db import models
import uuid
from datetime import timedelta


class Plano(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(
        'clientes.Cliente', verbose_name="cliente",
        on_delete=models.CASCADE,
        related_name='planos_cliente', blank=False, null=False)
    produto = models.ForeignKey(
        'produtos.Produto', verbose_name="produto",
        on_delete=models.CASCADE,
        related_name='planos_produto', blank=False, null=False)
    aporte = models.DecimalField("aporte", decimal_places=2, max_digits=10)
    data_da_contratacao = models.DateTimeField("data da contratacao", blank=False, null=False)
    idade_de_aposentadoria = models.IntegerField("idade de aposentadoria", blank=False, null=False)
    created = models.DateTimeField("criado", auto_now_add=True)
    updated = models.DateTimeField("alterado", auto_now=True)

    @property
    def saldo(self):
        return self.aportes_planos.all().aggregate(models.Sum('valor_aporte', default=0))['valor_aporte__sum'] + self.aporte

    @property
    def proximo_resgate(self):
        ultimo_resgate = self.resgates_plano.last()
        if ultimo_resgate:
            return ultimo_resgate.created + timedelta(days=self.produto.carencia_entre_resgates)
        else:
            return self.data_da_contratacao + timedelta(days=self.produto.carencia_inicial_de_resgate)

    def __str__(self):
        return f"{self.pk}"


class Aporte(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(
        'clientes.Cliente', verbose_name="cliente",
        on_delete=models.CASCADE,
        related_name='aportes_cliente', blank=False, null=False)
    plano = models.ForeignKey(
        Plano, verbose_name="aportes_plano",
        on_delete=models.CASCADE,
        related_name='aportes_planos', blank=False, null=False)
    valor_aporte = models.DecimalField("aporte", decimal_places=2, max_digits=10)

    created = models.DateTimeField("criado", auto_now_add=True)
    updated = models.DateTimeField("alterado", auto_now=True)

    def __str__(self):
        return f"Aporte {self.pk}"


class Resgate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plano = models.ForeignKey(
        Plano, verbose_name="plano",
        on_delete=models.CASCADE,
        related_name='resgates_plano', blank=False, null=False)
    valor_resgate = models.DecimalField("valor resgate", decimal_places=2, max_digits=10)

    created = models.DateTimeField("criado", auto_now_add=True)
    updated = models.DateTimeField("alterado", auto_now=True)

    def __str__(self):
        return f"Aporte {self.pk}"
