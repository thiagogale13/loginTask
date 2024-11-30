from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

class CustomUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('nombre_de_usuario', 'correo_electronico', 'edad')

class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('nombre_de_usuario', 'correo_electronico', 'edad', 'password', 'esta_activo', 'es_superusuario')

class LoginForm(forms.Form):
    correo_electronico = forms.EmailField(label='Dirección de correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
