from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
import json


class ClienteAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.payload = {
            "cpf": "53862500004",
            "nome": "Tony Stark",
            "email": "tony@email.com",
            "dataDeNascimento": "1986-01-01T12:00:00.000Z",
            "genero": "Masculino",
            "rendaMensal": 2899.5
        }

    def test_criar_cliente(self):
        response = self.client.post(
            '/clientes/',
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)