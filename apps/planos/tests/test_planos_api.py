from rest_framework import status
from rest_framework.test import APIClient
import json
from .base import PlanoBaseAPITest


class PlanoAPITest(PlanoBaseAPITest):
    
    def test_contratar_plano_valido(self):
        response = self.client.post(
            '/planos/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "produto": str(self.produto_valido.id),
                "aporte": 1500.00,
                "data_da_contratacao": "2024-06-01T12:00:00.000Z",
                "idade_de_aposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_contratar_plano_expirado(self):
        response = self.client.post(
            '/planos/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "produto": str(self.produto_invalido.id),
                "aporte": 1500.00,
                "data_da_contratacao": "2024-06-01T12:00:00.000Z",
                "idade_de_aposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_contratar_plano_sem_aporte_minimo(self):
        response = self.client.post(
            '/planos/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "produto": str(self.produto_valido.id),
                "aporte": 500.00,
                "data_da_contratacao": "2024-06-01T12:00:00.000Z",
                "idade_de_aposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_contratar_plano_sem_idade_minima(self):
        response = self.client.post(
            '/planos/',
            data=json.dumps({
                "cliente": str(self.cliente_1.id),
                "produto": str(self.produto_valido.id),
                "aporte": 1500.00,
                "data_da_contratacao": "2024-06-01T12:00:00.000Z",
                "idade_de_aposentadoria": 60
            }),
            content_type='application/json'
        )


        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
