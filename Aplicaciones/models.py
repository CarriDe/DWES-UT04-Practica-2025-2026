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
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    evaluacion = models.BooleanField(default=False)
    validada = models.BooleanField(default=False)
    profesor_validar = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='tareas_validadas')
    completada = models.BooleanField(default=False)
    crear = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas', null=True, blank=True)
    
    def __str__(self):
        return self.titulo