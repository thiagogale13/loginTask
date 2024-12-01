from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import CustomUserCreationForm, LoginForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            correo_electronico = form.cleaned_data.get('correo_electronico')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(correo_electronico=correo_electronico, password=raw_password)
            login(request, user)
            return redirect('tasks:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo_electronico = form.cleaned_data.get('correo_electronico')
            password = form.cleaned_data.get('password')
            user = authenticate(request, correo_electronico=correo_electronico, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks:index')
            else:
                messages.error(request, 'Correo electrónico o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')

@login_required
def account_detail(request):
    return render(request, 'accounts/account_detail.html')

@login_required
def account_edit(request):
    if request.method == 'POST':
        user = request.user
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:account_detail')
    else:
        user = request.user
        form = CustomUserChangeForm(instance=user)
    return render(request, 'accounts/account_edit.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Su contraseña ha sido actualizada exitosamente!')
            return redirect('accounts:account_detail')
        else:
            messages.error(request, 'Por favor corrija el error abajo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Su cuenta ha sido eliminada.')
        return redirect('accounts:register')
    return render(request, 'accounts/delete_account.html')
