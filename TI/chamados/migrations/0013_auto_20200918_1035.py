# Generated by Django 3.1 on 2020-09-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0012_auto_20200918_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='situacao',
            field=models.IntegerField(default=1, verbose_name='situacao'),
        ),
    ]
