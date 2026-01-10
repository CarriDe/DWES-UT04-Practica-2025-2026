from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import UsuarioForm, TareaForm

def lista_usuarios(request):
    alumnos = Usuario.objects.filter(rol='ALUMNO')
    profesores = Usuario.objects.filter(rol='PROFESOR')
    return render(request, 'Aplicaciones/lista_usuarios.html', {
        'alumnos': alumnos,
        'profesores': profesores
    })

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['contraseña'])
            usuario.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'Aplicaciones/crear_usuario.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        Usuario = request.POST.get('usuario')
        Contraseña = request.POST.get('contraseña')
        user = authenticate(request, username=Usuario, password=Contraseña)
    return render(request, 'Aplicaciones/login.html')

def crear_tarea_individual(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.tipo = 'INDIVIDUAL'  # Forzar tipo individual
            tarea.save()
            return redirect('lista_usuarios')
    else:
        form = TareaForm(initial={'tipo': 'INDIVIDUAL'})

    return render(request, 'Aplicaciones/crear_tarea_individual.html', {'form': form})

def crear_tarea_grupal(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.tipo = 'GRUPAL'  # Forzar tipo grupal
            tarea.save()
            return redirect('lista_usuarios')
    else:
        form = TareaForm(initial={'tipo': 'GRUPAL'})

    return render(request, 'Aplicaciones/crear_tarea_grupal.html', {'form': form})