from django.contrib import admin
from django.urls import path
from Aplicaciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('indice/', views.indice, name='indice'),
    path('lista/', views.lista_usuarios, name='lista_usuarios'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('crear-tarea-individual/', views.crear_tarea_individual, name='crear_tarea_individual'),
    path('crear-tarea-grupal/', views.crear_tarea_grupal, name='crear_tarea_grupal'),
    path('ejercicios-alumnos/', views.ejercicios_alumnos, name='ejercicios_alumnos'),
    path('validar-tarea/<int:tarea_id>/', views.validar_tarea, name='validar_tarea'),
    path('validar-tarea-profesor/<int:tarea_id>/', views.validar_tarea_profesor, name='validar_tarea_profesor'),
    path('validacion-profesor/', views.validacion, name='validacion_profesor'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
]
