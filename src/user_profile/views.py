# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm,UserCreationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from main.models import UserExtendData 
from .forms import EditProfileForm

# Create your views here.

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

def change_password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, data=request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            update_session_auth_hash(request, password_change_form.user) # dont logout the user.
            messages.success(request, "Password changed.")
            return redirect("/")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        password_change_form = PasswordChangeForm(request.user)
    data = {
        'password_change_form': password_change_form
    }
    return render(request, "change_password.html", data)

@login_required
def profile(request):
    user = request.user
    edit_profile_form = EditProfileForm(instance=user)
    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=user)
        if edit_profile_form.is_valid():
            print('edit_profile_form.is_valid')
            edit_profile_form.save()
            tel_no = edit_profile_form.cleaned_data.get('tel_no')
            address = edit_profile_form.cleaned_data.get('address')
            id_num = edit_profile_form.cleaned_data.get('id_num')
            user_extend = UserExtendData.objects.get(user_id=user.pk)
            user_extend.address = address
            user_extend.tel_no = tel_no
            user_extend.id_num = id_num
            user_extend.picture = "user_pic/"+request.POST["pic-input"]
            user_extend.save()
            return redirect(reverse('user_profile:profile'))
        else:
            print(edit_profile_form.errors)
       
    context = {
        'edit_profile_form': edit_profile_form,
        'user_extend' : UserExtendData.objects.get(user_id=user.pk)
    }
    return render(request, 'profile.html', context)

def success(request):
    return redirect('/')

def cancel(request):
    return redirect('/accounts/profile')