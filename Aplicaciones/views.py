from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Usuario, Tarea
from .forms import UsuarioForm, TareaForm, TareaGrupalForm

# Vista para mostrar el índice con todos los enlaces
def indice(request):
    return render(request, 'Aplicaciones/indice.html')

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
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        user = authenticate(request, username=usuario, password=contraseña)
        
        if user is not None:
            login(request, user)
            # Redirigir al perfil del usuario
            return redirect('perfil_usuario')
        else:
            # Credenciales inválidas, mostrar error
            return render(request, 'Aplicaciones/login.html', {'error': 'Usuario o contraseña incorrectos'})
    
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
# Vista para mostrar las tareas del alumno (individuales y grupales)
def ejercicios_alumnos(request):
    # Verificar que el usuario esté autenticado
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Obtener todas las tareas (individuales y grupales)
    # En este caso, mostramos todas las tareas ya que no hay relación directa
    # entre Usuario y Tarea de asignación
    tareas_individuales = Tarea.objects.filter(tipo='INDIVIDUAL').select_related('crear', 'profesor_validar')
    tareas_grupales = Tarea.objects.filter(tipo='GRUPAL').select_related('crear', 'profesor_validar')
    
    context = {
        'alumno': request.user,
        'tareas_individuales': tareas_individuales,
        'tareas_grupales': tareas_grupales
    }
    
    return render(request, 'Aplicaciones/ejercicios_alumnos.html', context)

# Vista para validar una tarea específica (acción de completar/entregar)
def validar_tarea(request, tarea_id):
    # Obtener la tarea o devolver error 404 si no existe
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    # Marcar la tarea como completada por el alumno
    tarea.completada = True
    tarea.save()
    
    # Redirigir de vuelta a la lista de tareas del alumno
    return redirect('ejercicios_alumnos')

# Vista para mostrar las tareas pendientes de validación para el profesor
def validacion(request):
    # Verificar que el usuario esté autenticado y sea profesor
    if not request.user.is_authenticated or request.user.rol != 'PROFESOR':
        return redirect('login')
    
    # Filtrar tareas que requieren validación y no están validadas
    tareas_pendientes = Tarea.objects.filter(
        validada=False,
        completada=True
    ).select_related('crear')
    
    context = {
        'profesor': request.user,
        'tareas_pendientes': tareas_pendientes
    }
    
    return render(request, 'Aplicaciones/validacion_profesor.html', context)

# Vista para mostrar el perfil del usuario
def perfil_usuario(request):
    # Verificar que el usuario esté autenticado
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'Aplicaciones/perfil_usuario.html')    