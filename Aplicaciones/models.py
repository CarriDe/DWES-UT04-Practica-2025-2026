from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('ALUMNO', 'Alumno'),
        ('PROFESOR', 'Profesor'),
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES)

    def __str__(self):
        return f"{self.usuario} ({self.rol})"

class Tarea(models.Model):
    TIPO_CHOICES = (
        ('INDIVIDUAL', 'Individual'),
        ('GRUPAL', 'Grupal'),
        ('EVALUABLE', 'Evaluable'),
    )
    
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()