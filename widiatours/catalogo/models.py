from django.db import models
from django.urls import reverse #redirecciona una url de un producto al browser
import uuid                     #se utiliza para definir atributos clave (pk)

# Create your models here.

class Compra(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Codigo unico del producto')
    name=models.CharField(max_length=100)
    precio=models.CharField('PRECIO', max_length=13)
    descripcion=models.CharField(max_length=200, null=True)


    def __str__(self):
        return f'{self.id} ({self.name}) ({self.descripcion})'