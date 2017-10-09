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
from .forms import EditProfileForm, top_up_form
# Create your views here.

# context = {
#     'id_num': 'id',
#     'tel_no': '098765',
#     'address': 'UserExtendData.address',
# }

# uncomment for database testing
# context = {
#     'id_num': UserExtendData.id_num,
#     'tel_no': UserExtendData.tel_no,
#     'address': UserExtendData.address,
# # }

# uncomment 1 line below for user profile login test

def top_up(request):
    if request.method == 'POST':
        form = top_up_form(request.POST)
        if form.is_valid():
            form.save()
            bill_pic = form.cleaned_data.get('bill_pic')
            user = request.user
            user_extend = UserExtendData.objects.get(user_id=user.pk)
            user_extend.bill_pic = bill_pic
            user_extend.save()
            return redirect(reverse('contact/'))
        return render(request, 'top_up.html', {'form': form})
    else:
        form = top_up_form(request.POST)
        return render(request, 'top_up.html', {'form': form})

@login_required
def profile(request):
    # context คือค่าที่ใช้ในการแสดงผลของ template
    # uncomment 2 lines below for user profile login test
    user = request.user
    user_extend = UserExtendData.objects.get(user_id=user.pk)
    context = {
        'id_num': user_extend.id_num,
        'tel_no': user_extend.tel_no,
        'address': user_extend.address,
    }
    template = 'profile.html'
    return render(request, template, context)

def change_password(request):
    context = locals()
    template = 'changepass.html'
    return render(request, template, context)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = form.PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', {
#         'form': form
#     })
@login_required
def profile_edit(request):
    if request.method == 'POST':
        # form = EditProfileForm(request.POST, instance=request.user)
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            tel_no = form.cleaned_data.get('tel_no')
            address = form.cleaned_data.get('address')
            user = request.user
            user_extend = UserExtendData.objects.get(user_id=user.pk)
            user_extend.address = address
            user_extend.tel_no = tel_no
            user_extend.save()
            return redirect(reverse('user_profile:profile'))
        else:
            print(form.errors)
            render(request, 'edit_profile.html', {'form': form})
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'edit_profile.html',{'form': form})

def success(request):
    return redirect('/accounts/profile')

def cancel(request):
    return redirect('/accounts/profile')
