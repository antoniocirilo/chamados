# Generated by Django 3.1 on 2020-09-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0009_chamado_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='comentario',
            field=models.TextField(default='Problema Resolvido', verbose_name='comentario'),
        ),
    ]
