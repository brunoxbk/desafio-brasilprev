from django.db import models
import uuid

class Cliente(models.Model):

    # "cpf": "45645645600",
    # "nome": "José da Silva",
    # "email": "jose@cliente.com",
    # "dataDeNascimento": "2010-08-24T12:00:00.000Z",
    # "genero": "Masculino",
    # "rendaMensal": 2899.5

    class GeneroChoices(models.TextChoices):
        Masculino = "Masculino"
        Feminino = "Feminino"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = models.CharField(
        "cpf", max_length=11, blank=False, null=False, unique=True)
    nome = models.CharField(
        "nome", max_length=120, blank=False, null=False)
    email = models.EmailField(
        "email", max_length=60, blank=False, null=False)
    dataDeNascimento = models.DateTimeField("data de nascimento", blank=False, null=False)
    genero = models.CharField(
        'genero', blank=False, max_length=10,
        null=False, choices=GeneroChoices.choices)
    rendaMensal = models.DecimalField("renda mensal", decimal_places=2, max_digits=10)

    created = models.DateTimeField("criado", auto_now_add=True)
    updated = models.DateTimeField("alterado", auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"
