from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'Aplicaciones/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        correo = request.POST.get('correo')
        rol = request.POST.get('rol')
        
        if usuario and contraseña and correo and rol:
            nuevo_usuario = Usuario.objects.create_user(username=usuario, password=contraseña, email=correo, rol=rol)
            return redirect('lista_usuarios')
    
    return render(request, 'Aplicaciones/crear_usuario.html')

def login_view(request):
    if request.method == 'POST':
        Usuario = request.POST.get('usuario')
        Contraseña = request.POST.get('contraseña')
        user = authenticate(request, username=Usuario, password=Contraseña)
    return render(request, 'Aplicaciones/login.html')

def crear_tarea(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        
        if tipo and titulo and descripcion:
            from .models import Tarea
            nueva_tarea = Tarea.objects.create(tipo=tipo, titulo=titulo, descripcion=descripcion)
            return redirect('lista_usuarios')
    
    return render(request, 'Aplicaciones/crear_tarea.html')