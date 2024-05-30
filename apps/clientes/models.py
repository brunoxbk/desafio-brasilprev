from django.db import models
from django.utils import timezone


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

    cpf = models.CharField(
        "cpf", max_length=11, blank=False, null=False, unique=True)
    nome = models.CharField(
        "nome", max_length=120, blank=False, null=False)
    email = models.EmailField(
        "email", max_length=60, blank=False, null=False)
    dataDeNascimento = models.DateTimeField("Data", blank=False, null=False)
    status = models.CharField(
        'genero', blank=False, max_length=10,
        null=False, choices=GeneroChoices.choices)
    rendaMensal = models.DecimalField("Renda mensal", decimal_places=2, max_digits=10)

    created = models.DateTimeField("Criado", auto_now_add=True)
    updated = models.DateTimeField("Alterado", auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"
