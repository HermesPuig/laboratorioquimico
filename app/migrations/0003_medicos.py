# Generated by Django 4.2.4 on 2023-11-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_usuario_tipodocumento_delete_tipodocumento'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombremedico', models.CharField(max_length=25)),
                ('especialidad', models.CharField(max_length=25)),
                ('MP', models.CharField(max_length=25)),
            ],
        ),
    ]
