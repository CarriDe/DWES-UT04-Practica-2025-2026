from django.contrib import admin
from django.urls import path
from Aplicaciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('lista/', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('crear-tarea-individual/', views.crear_tarea_individual, name='crear_tarea_individual'),
    path('crear-tarea-grupal/', views.crear_tarea_grupal, name='crear_tarea_grupal'),
    
]
