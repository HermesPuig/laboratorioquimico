# Generated by Django 4.2.7 on 2023-12-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudio',
            name='valor_hallado',
            field=models.CharField(max_length=50, null=True, verbose_name='Valor Hallado'),
        ),
        migrations.DeleteModel(
            name='Resultado',
        ),
    ]
