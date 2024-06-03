from django.db import models
import uuid
from datetime import timedelta


class Plano(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idCliente = models.ForeignKey(
        'clientes.Cliente', verbose_name="cliente",
        on_delete=models.CASCADE,
        related_name='planos_cliente', blank=False, null=False)
    idProduto = models.ForeignKey(
        'produtos.Produto', verbose_name="produto",
        on_delete=models.CASCADE,
        related_name='planos_produto', blank=False, null=False)
    aporte = models.DecimalField("aporte", decimal_places=2, max_digits=10)
    dataDaContratacao = models.DateTimeField("data da contratacao", blank=False, null=False)
    idadeDeAposentadoria = models.IntegerField("idade de aposentadoria", blank=False, null=False)
    created = models.DateTimeField("criado", auto_now_add=True)
    updated = models.DateTimeField("alterado", auto_now=True)

    @property
    def saldo(self):
        return self.aportes_planos.all().aggregate(models.Sum('valorAporte',default=0))['valorAporte__sum'] + self.aporte

    @property
    def proximo_resgate(self):
        ultimo_resgate = self.resgates_plano.last()
        if ultimo_resgate:
            return ultimo_resgate.created + timedelta(days=self.idProduto.carenciaEntreResgates)
        else:
            return self.dataDaContratacao + timedelta(days=self.idProduto.carenciaInicialDeResgate)

    def __str__(self):
        return f"{self.pk}"


class Aporte(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idCliente = models.ForeignKey(
        'clientes.Cliente', verbose_name="cliente",
        on_delete=models.CASCADE,
        related_name='aportes_cliente', blank=False, null=False)
    idPlano = models.ForeignKey(
        Plano, verbose_name="aportes_plano",
        on_delete=models.CASCADE,
        related_name='aportes_planos', blank=False, null=False)
    valorAporte = models.DecimalField("aporte", decimal_places=2, max_digits=10)

    created = models.DateTimeField("criado", auto_now_add=True)
    updated = models.DateTimeField("alterado", auto_now=True)

    def __str__(self):
        return f"Aporte {self.pk}"


class Resgate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idPlano = models.ForeignKey(
        Plano, verbose_name="plano",
        on_delete=models.CASCADE,
        related_name='resgates_plano', blank=False, null=False)
    valorResgate = models.DecimalField("resgate", decimal_places=2, max_digits=10)

    created = models.DateTimeField("criado", auto_now_add=True)
    updated = models.DateTimeField("alterado", auto_now=True)

    def __str__(self):
        return f"Aporte {self.pk}"
