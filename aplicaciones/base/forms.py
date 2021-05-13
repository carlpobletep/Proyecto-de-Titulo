from django.forms import ModelForm
#importamos las funciones de registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class createUserForm(UserCreationForm):
    error_messages = {
            'password_mismatch': '¡Deben de Coincidir las contraseñas, Intente nuevamente!'
        }
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
        widgets = {

            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Aqui va Su Nombre',
            }),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus Apellidos',
            }),

            'username': forms.TextInput(attrs={
                'placeholder':'Usuario',
            }), 

            'email': forms.EmailInput(attrs={
                'placeholder':'Aqui_va_el_Correo@gmail.com',
            })
        }
        error_messages = {
            'username': {
                'unique': '¡El Usuario ya existe, pruebe con otro!',
            }
        }