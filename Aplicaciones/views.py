from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate
from .forms import UsuarioForm, TareaForm, TareaGrupalForm
from .models import Tarea
from django.shortcuts import get_object_or_404

# Vista para listar todos los usuarios separados por rol
def lista_usuarios(request):
    alumnos = Usuario.objects.filter(rol='ALUMNO')
    profesores = Usuario.objects.filter(rol='PROFESOR')
    return render(request, 'Aplicaciones/lista_usuarios.html', {
        'alumnos': alumnos,
        'profesores': profesores
    })

# Vista para listar todas las tareas
def lista_tareas(request):
    tareas_individual = Tarea.objects.filter(tipo='INDIVIDUAL')
    tareas_grupal = Tarea.objects.filter(tipo='GRUPAL')
    return render(request, 'Aplicaciones/lista_tareas.html', {
        'tareas_individual': tareas_individual,
        'tareas_grupal': tareas_grupal
    })

# Vista para crear un nuevo usuario, para el formulario de registro y aplicar el hash a la contraseña
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Guardar para poder modificar la contraseña
            usuario = form.save(commit=False)
            # Aplicar hash a la contraseña antes de guardar
            usuario.set_password(form.cleaned_data['contraseña'])
            usuario.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'Aplicaciones/crear_usuario.html', {'form': form})


# Vista para iniciar sesión, autentificaa las credenciales de la base de datos
def login_view(request):
    if request.method == 'POST':
        Usuario = request.POST.get('usuario')
        Contraseña = request.POST.get('contraseña')
        user = authenticate(request, username=Usuario, password=Contraseña)
    return render(request, 'Aplicaciones/login.html')

# Vista para crear una tarea individual
def crear_tarea_individual(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.tipo = 'INDIVIDUAL'
            tarea.save()
            return redirect('lista_tareas')
    else:
        # Inicializar formulario
        form = TareaForm(initial={'tipo': 'INDIVIDUAL'})

    return render(request, 'Aplicaciones/crear_tarea_individual.html', {'form': form})

# Vista para crear una tarea grupal
def crear_tarea_grupal(request):
    if request.method == 'POST':
        form = TareaGrupalForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.tipo = 'GRUPAL'  # Forzar tipo grupal
            tarea.save()
            return redirect('lista_tareas')
    else:
        # Inicializar formulario
        form = TareaGrupalForm(initial={'tipo': 'GRUPAL'})

    return render(request, 'Aplicaciones/crear_tarea_grupal.html', {'form': form})

# Vista para validar tareas pendientes
def validar_tarea(request, tarea_id):
    # Obtener la tarea o devolver error 404 si no existe
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        # Marcar la tarea como validada
        tarea.validada = True
        tarea.profesor_validar = request.user
        tarea.save()
        return redirect('lista_usuarios')
    
    return render(request, 'Aplicaciones/validar_tarea.html', {'tarea': tarea})

def validacion(request):
    tareas = Tarea.objects.filter(requiere_evaluacion=True, completada=True, validada=False)
    return render(request, 'Aplicaciones/validacion.html', {'tareas': tareas})    