from django import forms
from .models import Usuario, Tarea

class UsuarioForm(forms.ModelForm):
    contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        # Campos reales del modelo AbstractUser extendido
        fields = ['username', 'first_name', 'last_name', 'email', 'rol']
        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            'rol': 'Rol',
        }

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'tipo', 'fecha_final', 'evaluacion']
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'tipo': 'Tipo',
            'fecha_final': 'Fecha límite',
            'evaluacion': 'Requiere evaluación del profesor',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'tipo': forms.HiddenInput(attrs={'value': 'INDIVIDUAL'}),
            'fecha_final': forms.DateInput(attrs={'type': 'date'}),
        }

class TareaGrupalForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'tipo', 'fecha_final', 'alumnos_participantes', 'evaluacion']
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'tipo': 'Tipo',
            'fecha_final': 'Fecha límite',
            'alumnos_participantes': 'Alumnos participantes',
            'evaluacion': 'Requiere evaluación del profesor',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'tipo': forms.HiddenInput(attrs={'value': 'GRUPAL'}),
            'fecha_final': forms.DateInput(attrs={'type': 'date'}),
            'alumnos_participantes': forms.CheckboxSelectMultiple(),
        }        