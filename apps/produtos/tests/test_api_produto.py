from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
import json


class ProdutoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.payload = {
            "nome": "Brasilprev Longo Prazo",
            "susep": "15414900840201816",
            "expiracao_de_venda": "2021-01-01T12:00:00.000Z",
            "valor_minimo_aporte_inicial": 1000.0,
            "valor_minimo_aporte_extra": 100.0,
            "idade_de_entrada": 18,
            "idade_de_saida": 60,
            "carencia_inicial_de_resgate": 60,
            "carencia_entre_resgates": 30
        }

    def test_criar_produto(self):
        response = self.client.post(
            '/produtos/',
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)