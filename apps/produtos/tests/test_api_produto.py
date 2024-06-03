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
            "expiracaoDeVenda": "2021-01-01T12:00:00.000Z",
            "valorMinimoAporteInicial": 1000.0,
            "valorMinimoAporteExtra": 100.0,
            "idadeDeEntrada": 18,
            "idadeDeSaida": 60,
            "carenciaInicialDeResgate": 60,
            "carenciaEntreResgates": 30
        }

    def test_criar_produto(self):
        response = self.client.post(
            '/produtos/',
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)