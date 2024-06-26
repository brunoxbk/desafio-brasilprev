# Generated by Django 5.0.6 on 2024-06-05 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='carenciaEntreResgates',
            new_name='carencia_entre_resgates',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='carenciaInicialDeResgate',
            new_name='carencia_inicial_de_resgate',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='expiracaoDeVenda',
            new_name='expiracao_de_venda',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='idadeDeEntrada',
            new_name='idade_de_entrada',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='idadeDeSaida',
            new_name='idade_de_saida',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='valorMinimoAporteExtra',
            new_name='valor_minimo_aporte_extra',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='valorMinimoAporteInicial',
            new_name='valor_minimo_aporte_inicial',
        ),
    ]
