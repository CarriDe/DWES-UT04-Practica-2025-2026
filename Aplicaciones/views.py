from django.shortcuts import render
from .models import Usuario
from django.contrib.auth import authenticate

def index(request):
    alumnos = Usuario.objects.filter(rol='ALUMNO')
    profesores = Usuario.objects.filter(rol='PROFESOR')
    return render(request, 'Aplicaciones/listapruebas.html', {'alumnos': alumnos, 'profesores': profesores})

def login_view(request):
    if request.method == 'POST':
        Usuario = request.POST.get('Usuario')
        Contraseña = request.POST.get('Contraseña')
        user = authenticate(request, username=Usuario, password=Contraseña)
    return render(request, 'Aplicaciones/login.html')