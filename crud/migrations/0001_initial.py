# Generated by Django 4.2 on 2024-05-15 19:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prospecto',
            fields=[
                ('id_prospecto', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('sexo', models.IntegerField(choices=[[1, 'Mujer'], [2, 'Hombre'], [0, 'Otro']])),
                ('estado_id', models.IntegerField(choices=[[0, 'Abierto'], [1, 'Perdido'], [2, 'Ganado']])),
                ('etapa_id', models.IntegerField(choices=[[0, 'En conversacion'], [1, 'Conseguido'], [2, 'Perdido']])),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.cliente')),
            ],
        ),
    ]