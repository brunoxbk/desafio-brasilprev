from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
import json
from apps.produtos.models import Produto
from apps.clientes.models import Cliente
from apps.planos.models import Plano
from datetime import datetime, timedelta


class PlanoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        dados_produto_valido = {
            "nome": "Brasilprev Longo Prazo",
            "susep": "15414900840201817",
            "expiracaoDeVenda": "2035-01-01T12:00:00.000Z",
            "valorMinimoAporteInicial": 1000.0,
            "valorMinimoAporteExtra": 100.0,
            "idadeDeEntrada": 28,
            "idadeDeSaida": 60,
            "carenciaInicialDeResgate": 60,
            "carenciaEntreResgates": 30
        }

        dados_produto_invalido = {
            "nome": "Brasilprev Longo Prazo",
            "susep": "15414900840201818",
            "expiracaoDeVenda": "2021-01-01T12:00:00.000Z",
            "valorMinimoAporteInicial": 1000.0,
            "valorMinimoAporteExtra": 100.0,
            "idadeDeEntrada": 18,
            "idadeDeSaida": 60,
            "carenciaInicialDeResgate": 60,
            "carenciaEntreResgates": 30
        }


        dados_cliente_1 = {
            "cpf": "53862500004",
            "nome": "Bruce Banner",
            "email": "bruce@email.com",
            "dataDeNascimento": "2006-01-01T12:00:00.000Z",
            "genero": "Masculino",
            "rendaMensal": 2899.5
        }

        dados_cliente_2 = {
            "cpf": "68166768070",
            "nome": "Peter Parker",
            "email": "peter@email.com",
            "dataDeNascimento": datetime.fromisoformat("1989-01-01T12:00:00.000+00:00"),
            "genero": "Masculino",
            "rendaMensal": 2899.5
        }

        self.produto_valido = Produto.objects.create(**dados_produto_valido)
        self.produto_invalido = Produto.objects.create(**dados_produto_invalido)
        self.cliente_1 = Cliente.objects.create(**dados_cliente_1)
        self.cliente_2 = Cliente.objects.create(**dados_cliente_2)

        dados_plano_invalido = {
            "idCliente": self.cliente_2,
            "idProduto": self.produto_invalido,
            "aporte": 1500.00,
            "dataDaContratacao": "2024-06-01T12:00:00.000Z",
            "idadeDeAposentadoria": 60
        }

        self.plano_invalido = Plano.objects.create(**dados_plano_invalido)

        dados_plano_sem_saldo = {
            "idCliente": self.cliente_2,
            "idProduto": self.produto_valido,
            "aporte": 0,
            "dataDaContratacao": "2024-06-01T12:00:00.000Z",
            "idadeDeAposentadoria": 60
        }

        self.plano_sem_saldo = Plano.objects.create(**dados_plano_sem_saldo)


    def test_contratar_plano_valido(self):
        response = self.client.post(
            '/planos/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idProduto": str(self.produto_valido.id),
                "aporte": 1500.00,
                "dataDaContratacao": "2024-06-01T12:00:00.000Z",
                "idadeDeAposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_contratar_plano_expirado(self):
        response = self.client.post(
            '/planos/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idProduto": str(self.produto_invalido.id),
                "aporte": 1500.00,
                "dataDaContratacao": "2024-06-01T12:00:00.000Z",
                "idadeDeAposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_contratar_sem_aporte_minimo(self):
        response = self.client.post(
            '/planos/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idProduto": str(self.produto_valido.id),
                "aporte": 500.00,
                "dataDaContratacao": "2024-06-01T12:00:00.000Z",
                "idadeDeAposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_contratar_plano_sem_idade_minima(self):
        response = self.client.post(
            '/planos/',
            data=json.dumps({
                "idCliente": str(self.cliente_1.id),
                "idProduto": str(self.produto_valido.id),
                "aporte": 1500.00,
                "dataDaContratacao": "2024-06-01T12:00:00.000Z",
                "idadeDeAposentadoria": 60
            }),
            content_type='application/json'
        )


        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_aporte_sem_valor_minimo(self):

        response_plano = self.client.post(
            '/planos/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idProduto": str(self.produto_valido.id),
                "aporte": 1500.00,
                "dataDaContratacao": "2024-06-01T12:00:00.000Z",
                "idadeDeAposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response_plano.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idPlano": response_plano.json()['id'],
                "valorAporte": 50.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_aporte_produto_inválido(self):


        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idPlano": str(self.plano_invalido.id),
                "valorAporte": 500.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_aporte_produto_sem_saldo(self):

        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idPlano": str(self.plano_sem_saldo.id),
                "valorAporte": 500.00
            }),
            content_type='application/json'
        )


        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_aporte_com_valor_minimo(self):

        response_plano = self.client.post(
            '/planos/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idProduto": str(self.produto_valido.id),
                "aporte": 1500.00,
                "dataDaContratacao": "2024-06-01T12:00:00.000Z",
                "idadeDeAposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response_plano.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idPlano": response_plano.json()['id'],
                "valorAporte": 150.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_resgate_sem_saldo(self):

        response_plano = self.client.post(
            '/planos/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idProduto": str(self.produto_valido.id),
                "aporte": 1500.00,
                "dataDaContratacao": "2024-06-01T12:00:00.000Z",
                "idadeDeAposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response_plano.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idPlano": response_plano.json()['id'],
                "valorAporte": 150.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idPlano": response_plano.json()['id'],
                "valorAporte": 150.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/resgates/',
            data=json.dumps({
                "idPlano": response_plano.json()['id'],
                "valorResgate": 2000.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_resgate_com_saldo(self):

        response_plano = self.client.post(
            '/planos/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idProduto": str(self.produto_valido.id),
                "aporte": 1500.00,
                "dataDaContratacao": "2024-01-01T12:00:00.000Z",
                "idadeDeAposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response_plano.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idPlano": response_plano.json()['id'],
                "valorAporte": 150.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/aportes/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idPlano": response_plano.json()['id'],
                "valorAporte": 150.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/resgates/',
            data=json.dumps({
                "idPlano": response_plano.json()['id'],
                "valorResgate": 1800.00
            }),
            content_type='application/json'
        )

        # print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_resgate_sem_carencia(self):
        date_obj = datetime.now() - timedelta(days=20)

        print(date_obj.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z')

        response_plano = self.client.post(
            '/planos/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idProduto": str(self.produto_valido.id),
                "aporte": 3500.00,
                "dataDaContratacao": date_obj.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
                "idadeDeAposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response_plano.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/resgates/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idPlano": response_plano.json()['id'],
                "valorResgate": 1500.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_resgate_com_carencia(self):
        date_obj = datetime.now() - timedelta(days=120)

        print(date_obj.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z')

        response_plano = self.client.post(
            '/planos/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idProduto": str(self.produto_valido.id),
                "aporte": 3500.00,
                "dataDaContratacao": date_obj.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
                "idadeDeAposentadoria": 60
            }),
            content_type='application/json'
        )

        self.assertEqual(response_plano.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/planos/resgates/',
            data=json.dumps({
                "idCliente": str(self.cliente_2.id),
                "idPlano": response_plano.json()['id'],
                "valorResgate": 1500.00
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)