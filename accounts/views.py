from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import (
    RegistrationForm, EditRegistrationForm, EditProfileForm, UploadPictureForm)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



def home(request):
    return redirect('music:index')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('accounts:about-groove')
        else:
            return redirect('accounts:register')
    else:
        form = RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})


def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form1 = EditRegistrationForm(data=request.POST, instance=user)
        form2 = EditProfileForm(data=request.POST, instance=user.profile)
        if all([form1.is_valid(), form2.is_valid()]):
            form1.save()
            form2.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile has been successfully edited.')
            return redirect('accounts:edit-profile')
        else:
            return redirect('accounts:edit-profile')
    else:
        form1 = EditRegistrationForm(instance=user)
        form2 = EditProfileForm(instance=user.profile)
        return render(request, 'accounts/edit-profile.html', {'form1': form1, 'form2': form2})


def edit_picture(request):
    user = request.user
    if request.method == 'POST':
        form = UploadPictureForm(data=request.POST, instance=user.profile, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully, updated your profile picture.')
            return redirect('accounts:edit-picture')
        else:
            messages.add_message(request, messages.ERROR, 'Please correct the error below.')
            return redirect('accounts:edit-picture')
    else:
        form = UploadPictureForm(instance=user.profile)
        return render(request, 'accounts/edit-picture.html', {'form': form})


def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your have successfully changed your password.')
            update_session_auth_hash(request, form.user)
            return redirect('accounts:edit-password')
        else:
            messages.add_message(request, messages.ERROR, 'Please correct the error below.')
            return redirect('accounts:edit-password')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/password.html', {'form': form})


def about_groove(request):
    return render(request, 'accounts/about.html')

