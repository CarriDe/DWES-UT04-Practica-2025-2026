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
        fields = ['titulo', 'descripcion', 'tipo']
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'tipo': 'Tipo',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'tipo': forms.HiddenInput(attrs={'value': 'INDIVIDUAL'}),
        }