# Generated by Django 3.1.1 on 2020-09-22 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0017_auto_20200922_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamado',
            name='situacao',
        ),
    ]
