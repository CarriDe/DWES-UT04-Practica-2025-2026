# DWES-UT04-Práctica (2025-2026)

Aplicación Django para gestionar usuarios (alumnos y profesores) con roles, autenticación básica y creación/listado de tareas.

## Puesta en marcha del proyecto

1. Creamos el proyecto de Github, lo clonamos a Visual Studio y escribimos el código.
2. Se instalan las dependencias: `pip install -r requirements.txt`
3. Se ejecutan las migraciones: `python manage.py migrate`
4. Se inicia el servidor: `python3 manage.py runserver`
5. Se accede a `http://127.0.0.1:8000/`

## Descripción del proyecto y sus funciones

Este proyecto permite gestionar un entorno educativo con **control de acceso por roles** (**ALUMNO** y **PROFESOR**), funciona desde la interfaz, no hace falta usar datos existentes.

# Gestión de usuarios

- Se puede crear usuarios con sus roles, profesor o alumno, desde la sección **Crear Usuario**
- Se muestran todos los usuarios registrados en **Lista de Usuarios**
- Autenticación real, cierre de sesión y protección de rutas para algunas secciones del proyecto (ejercicios y validaciones de profesores) según el rol del usuario

# Gestión de tareas

- Creación de tareas por parte del profesor desde el **Índice**
- Tipos de tareas: Individuales y Ggrupales, en estas se pueden asignar los alumnos que participarán
- Seguimiento del estado de las tareas: Pendiente, entregada y validada (por un profesor)  

# Funcionalidades para los usuarios

- Visualización del **perfil personal**
- Consulta de **ejercicios y tareas pendientes** para los alumnos y **Validación de Tareas** para los profesores.
- Entrega de tareas desde la sección **Ejercicios y Tareas** para los alumnos y **validación de las entregas** para los profesores
- Consultar el **estado de las tareas** es posible para todos los roles

Esto hace que el trabajo sea más claro, seguro y operativo desde la interfaz de la aplicación.

## Tecnologías usadas

- Python
- Django
- SQLite
- GitHub

## Estructura
- `Aplicaciones/` (app principal, incluye los modelos, vistas, formularios y templates html)
- `Tareas/` (configuración de proyecto y rutas)
