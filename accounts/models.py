from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, correo_electronico, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El correo electrónico es obligatorio')
        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(correo_electronico=correo_electronico, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_electronico, password=None, **extra_fields):
        extra_fields.setdefault('es_superusuario', True)
        extra_fields.setdefault('es_personal', True)

        if extra_fields.get('es_superusuario') is not True:
            raise ValueError('Superusuario debe tener es_superusuario=True.')
        if extra_fields.get('es_personal') is not True:
            raise ValueError('Superusuario debe tener es_personal=True.')

        return self.create_user(correo_electronico, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    nombre_de_usuario = models.CharField(max_length=150)
    correo_electronico = models.EmailField(unique=True)
    edad = models.PositiveIntegerField(default=0)
    es_superusuario = models.BooleanField(default=False)
    es_personal = models.BooleanField(default=False)
    esta_activo = models.BooleanField(default=True)
    fecha_union = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre_de_usuario']

    objects = CustomUserManager()

    def __str__(self):
        return self.correo_electronico

    def has_perm(self, perm, obj=None):
        return self.es_superusuario

    def has_module_perms(self, app_label):
        return self.es_superusuario
