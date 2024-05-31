from django.db import models
import uuid

class Plano(models.Model):
    # {
    # "idCliente": "18dfeb91-459a-4bc7-9cdd-d93b41f7bf62",
    # "idProduto": "30f6b23f-c93d-4cf9-8916-bcdb9fac83df",
    # "aporte": 2000.00,
    # "dataDaContratacao": "2022-04-05T12:00:00.000Z",
    # "idadeDeAposentadoria": 60
    # }
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

    def __str__(self):
        return f"{self.pk}"