from django.db import models

# Create your models here.

class Ramos(models.Model):
    nombre = models.CharField(max_length=30)
    horario = models.CharField(max_length=30)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre