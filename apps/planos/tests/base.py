from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
import json
from apps.produtos.models import Produto
from apps.clientes.models import Cliente
from apps.planos.models import Plano
from datetime import datetime, timedelta


class PlanoBaseAPITest(TestCase):
    
    def setUp(self):
        self.client = APIClient()

        dados_produto_valido = {
            "nome": "Brasilprev Longo Prazo",
            "susep": "15414900840201817",
            "expiracao_de_venda": "2035-01-01T12:00:00.000Z",
            "valor_minimo_aporte_inicial": 1000.0,
            "valor_minimo_aporte_extra": 100.0,
            "idade_de_entrada": 28,
            "idade_de_saida": 60,
            "carencia_inicial_de_resgate": 60,
            "carencia_entre_resgates": 30
        }

        dados_produto_invalido = {
            "nome": "Brasilprev Longo Prazo",
            "susep": "15414900840201818",
            "expiracao_de_venda": "2021-01-01T12:00:00.000Z",
            "valor_minimo_aporte_inicial": 1000.0,
            "valor_minimo_aporte_extra": 100.0,
            "idade_de_entrada": 18,
            "idade_de_saida": 60,
            "carencia_inicial_de_resgate": 60,
            "carencia_entre_resgates": 30
        }


        dados_cliente_1 = {
            "cpf": "53862500004",
            "nome": "Bruce Banner",
            "email": "bruce@email.com",
            "data_de_nascimento": "2006-01-01T12:00:00.000Z",
            "genero": "Masculino",
            "renda_mensal": 2899.5
        }

        dados_cliente_2 = {
            "cpf": "68166768070",
            "nome": "Peter Parker",
            "email": "peter@email.com",
            "data_de_nascimento": datetime.fromisoformat("1989-01-01T12:00:00.000+00:00"),
            "genero": "Masculino",
            "renda_mensal": 2899.5
        }

        self.produto_valido = Produto.objects.create(**dados_produto_valido)
        self.produto_invalido = Produto.objects.create(**dados_produto_invalido)
        self.cliente_1 = Cliente.objects.create(**dados_cliente_1)
        self.cliente_2 = Cliente.objects.create(**dados_cliente_2)

        dados_plano_invalido = {
            "cliente": self.cliente_2,
            "produto": self.produto_invalido,
            "aporte": 1500.00,
            "data_da_contratacao": "2024-06-01T12:00:00.000Z",
            "idade_de_aposentadoria": 60
        }

        self.plano_invalido = Plano.objects.create(**dados_plano_invalido)

        dados_plano_sem_saldo = {
            "cliente": self.cliente_2,
            "produto": self.produto_valido,
            "aporte": 0,
            "data_da_contratacao": "2024-06-01T12:00:00.000Z",
            "idade_de_aposentadoria": 60
        }

        self.plano_sem_saldo = Plano.objects.create(**dados_plano_sem_saldo)

