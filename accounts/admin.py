from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    list_display = ('correo_electronico', 'nombre_de_usuario', 'edad', 'es_superusuario', 'esta_activo')
    list_filter = ('es_superusuario',)
    fieldsets = (
        (None, {'fields': ('correo_electronico', 'password')}),
        ('Información Personal', {'fields': ('nombre_de_usuario', 'edad')}),
        ('Permisos', {'fields': ('es_superusuario', 'es_personal', 'esta_activo')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('correo_electronico', 'nombre_de_usuario', 'edad', 'password1', 'password2'),
        }),
    )
    search_fields = ('correo_electronico',)
    ordering = ('correo_electronico',)
    filter_horizontal = ()

admin.site.register(CustomUser, UserAdmin)

