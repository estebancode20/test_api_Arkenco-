from django.db import models

# Create your models here.
import uuid
from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_empresa = models.CharField(max_length=255)
    rut = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        fila = f"{self.nombre_empresa} - rut: {self.rut}"
        return fila
    

opciones_sexo = [
[1,"Mujer"],
[2,"Hombre"],
[0,"Otro"]

]




opciones_estado = [
[0,"Abierto"],
[1,"Perdido"],
[2,"Ganado"]
]
"""
class Estado(models.Model):
    id_estado = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estado = models.IntegerField(choices=opciones_estado)
"""



opciones_etapa = [
[0,"En conversacion"],
[1,"Conseguido"],
[2,"Perdido"]
]
"""
class Etapa(models.Model):
    id_etapa = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    etapa = models.IntegerField(choices=opciones_etapa)    
"""


class Prospecto(models.Model):
    id_prospecto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    sexo = models.IntegerField(choices=opciones_sexo)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado_id = models.IntegerField(choices=opciones_estado)
    etapa_id = models.IntegerField(choices=opciones_etapa)