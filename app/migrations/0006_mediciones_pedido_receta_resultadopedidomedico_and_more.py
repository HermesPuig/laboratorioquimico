# Generated by Django 4.2.4 on 2023-11-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mediciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombremedicamento', models.CharField(max_length=25)),
                ('cantML', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, verbose_name='nombre pedido:')),
                ('descripcion', models.CharField(max_length=25, verbose_name='descripcion pedido')),
                ('receta', models.CharField(max_length=25, verbose_name='receta pedido')),
            ],
        ),
        migrations.CreateModel(
            name='receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analisissolicitado', models.CharField(max_length=25, verbose_name='analisis receta')),
                ('medicamentosolicitado', models.CharField(max_length=25)),
                ('nombremedico', models.CharField(max_length=25)),
                ('fecha', models.DateField(max_length=25)),
                ('MP', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='resultadopedidomedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=25)),
                ('documento', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='reseta',
            name='paciente',
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
        migrations.DeleteModel(
            name='Reseta',
        ),
    ]
