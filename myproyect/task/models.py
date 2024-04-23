from django.db import models
import datetime
from time import timezone


class Task(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateTimeField("fecha limite")
    estado = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    def was_published_recently(self):
        return self.fecha_limite >= timezone.now() - datetime.timedelta(days=1)