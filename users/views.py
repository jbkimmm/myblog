from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from users.forms import (
    RegistrationForm,
    EditProfileForm)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/profile.html', args)

def edit_profile(request,pk=None):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            args = {'form': form}
        # return render(request, 'users/edit_profile.html', {'form': form})
            # args = {'user': user}
            return render(request, 'users/profile.html', args)
    else:
        form = EditProfileForm(instance=request.user)
        if pk:
            user = User.objects.get(pk=pk)
        else:
            user = request.user
        args = {'user': user}
        return render(request, 'users/view_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            args = {'form': form}
            update_session_auth_hash(request, form.user)
            return render(request, 'users/profile.html', args)
        else:
            return render(request, 'users/change_password.html', args)
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'users/change_password.html', args)
