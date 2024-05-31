# Generated by Django 5.0.6 on 2024-05-31 22:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=120, verbose_name='nome')),
                ('susep', models.CharField(max_length=60, verbose_name='susep')),
                ('expiracaoDeVenda', models.DateTimeField(verbose_name='expiração de venda')),
                ('valorMinimoAporteInicial', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='valor minimo aporte inicial')),
                ('valorMinimoAporteExtra', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='valor minimo aporte extra')),
                ('idadeDeEntrada', models.IntegerField(verbose_name='idade entrada')),
                ('idadeDeSaida', models.IntegerField(verbose_name='idade entrada')),
                ('carenciaInicialDeResgate', models.IntegerField(verbose_name='carência inicial')),
                ('carenciaEntreResgates', models.IntegerField(verbose_name='carência entre resgates')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='alterado')),
            ],
        ),
    ]
