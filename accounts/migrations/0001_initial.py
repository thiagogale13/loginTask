# Generated by Django 4.2.16 on 2024-11-30 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre_de_usuario', models.CharField(max_length=150)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
                ('edad', models.PositiveIntegerField(default=0)),
                ('es_superusuario', models.BooleanField(default=False)),
                ('es_personal', models.BooleanField(default=False)),
                ('esta_activo', models.BooleanField(default=True)),
                ('fecha_union', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
