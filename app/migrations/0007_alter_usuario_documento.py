# Generated by Django 4.2.4 on 2023-11-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_mediciones_pedido_receta_resultadopedidomedico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='documento',
            field=models.IntegerField(max_length=25),
        ),
    ]
