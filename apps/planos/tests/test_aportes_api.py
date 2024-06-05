from rest_framework import status
from rest_framework.test import APIClient
import json
from .base import PlanoBaseAPITest


class AporteAPITest(PlanoBaseAPITest):
    

    def test_aporte_sem_valor_minimo(self):

        response_plano = self.client.post(
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

        self.assertEqual(response_plano.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "plano": response_plano.json()['id'],
                "valor_aporte": 50.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_aporte_produto_inválido(self):


        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "plano": str(self.plano_invalido.id),
                "valor_aporte": 500.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_aporte_produto_sem_saldo(self):

        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "plano": str(self.plano_sem_saldo.id),
                "valor_aporte": 500.00
            }),
            content_type='application/json'
        )


        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_aporte_com_valor_minimo(self):

        response_plano = self.client.post(
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

        self.assertEqual(response_plano.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "plano": response_plano.json()['id'],
                "valor_aporte": 150.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    