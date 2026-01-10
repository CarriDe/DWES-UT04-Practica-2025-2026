from django.contrib import admin
from django.urls import path
from Aplicaciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('lista/', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('crear-tarea/', views.crear_tarea, name='crear_tarea'),
    
]
