# Generated by Django 5.0.6 on 2024-06-05 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planos', '0003_resgate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aporte',
            old_name='idCliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='aporte',
            old_name='idPlano',
            new_name='plano',
        ),
        migrations.RenameField(
            model_name='aporte',
            old_name='valorAporte',
            new_name='valor_aporte',
        ),
        migrations.RenameField(
            model_name='plano',
            old_name='idCliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='plano',
            old_name='dataDaContratacao',
            new_name='data_da_contratacao',
        ),
        migrations.RenameField(
            model_name='plano',
            old_name='idadeDeAposentadoria',
            new_name='idade_de_aposentadoria',
        ),
        migrations.RenameField(
            model_name='plano',
            old_name='idProduto',
            new_name='produto',
        ),
        migrations.RemoveField(
            model_name='resgate',
            name='idPlano',
        ),
        migrations.RemoveField(
            model_name='resgate',
            name='valorResgate',
        ),
        migrations.AddField(
            model_name='resgate',
            name='plano',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='resgates_plano', to='planos.plano', verbose_name='plano'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resgate',
            name='valor_resgate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='valor resgate'),
            preserve_default=False,
        ),
    ]