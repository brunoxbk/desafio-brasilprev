from rest_framework import status
from rest_framework.test import APIClient
import json
from .base import PlanoBaseAPITest
from datetime import datetime, timedelta


class ResgateAPITest(PlanoBaseAPITest):
    
    def test_resgate_sem_saldo(self):

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

        response = self.client.post(
            '/planos/resgates/',
            data=json.dumps({
                "plano": response_plano.json()['id'],
                "valor_resgate": 2000.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_resgate_com_saldo(self):

        response_plano = self.client.post(
            '/planos/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "produto": str(self.produto_valido.id),
                "aporte": 1500.00,
                "data_da_contratacao": "2024-01-01T12:00:00.000Z",
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

        response = self.client.post(
            '/planos/resgates/',
            data=json.dumps({
                "plano": response_plano.json()['id'],
                "valor_resgate": 1800.00
            }),
            content_type='application/json'
        )


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_resgate_sem_carencia(self):
        date_obj = datetime.now() - timedelta(days=20)

        response_plano = self.client.post(
            '/planos/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "produto": str(self.produto_valido.id),
                "aporte": 3500.00,
                "data_da_contratacao": date_obj.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
                "idade_de_aposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response_plano.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/resgates/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "plano": response_plano.json()['id'],
                "valor_resgate": 1500.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_resgate_com_carencia(self):
        date_obj = datetime.now() - timedelta(days=120)

        response_plano = self.client.post(
            '/planos/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "produto": str(self.produto_valido.id),
                "aporte": 3500.00,
                "data_da_contratacao": date_obj.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
                "idade_de_aposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response_plano.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/resgates/',
            data=json.dumps({
                "cliente": str(self.cliente_2.id),
                "plano": response_plano.json()['id'],
                "valor_resgate": 1500.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
