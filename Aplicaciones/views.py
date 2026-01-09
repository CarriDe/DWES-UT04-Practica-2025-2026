from django.shortcuts import render
from .models import Usuario

def index(request):
    alumnos = Usuario.objects.filter(rol='ALUMNO')
    profesores = Usuario.objects.filter(rol='PROFESOR')
    return render(request, 'Aplicaciones/listapruebas.html', {'alumnos': alumnos, 'profesores': profesores})
