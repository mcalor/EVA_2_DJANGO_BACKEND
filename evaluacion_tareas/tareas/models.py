from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator



class Tarea(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    prioridad = models.IntegerField(validators=[MinValueValidator(3)])
    vigente = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_limite = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.titulo} [{self.prioridad}]"