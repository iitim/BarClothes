# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from main.models import UserExtendData 

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from forms import EditProfileForm
# Create your views here.

context = {
    'id_num': 'id',
    'tel_no': '098765',
    'address': 'UserExtendData.address',
}

# uncomment for database testing
# context = {
#     'id_num': UserExtendData.id_num,
#     'tel_no': UserExtendData.tel_no,
#     'address': UserExtendData.address,
# # }

# uncomment 1 line below for user profile login test
# @login_required
def profile(request):
    # context คือค่าที่ใช้ในการแสดงผลของ template
    # uncomment 2 lines below for user profile login test
    # user = request.user,
    # context.update({'user':user})
    template = 'profile.html'
    return render(request, template, context)

def change_password(request):
    context = locals()
    template = 'changepass.html'
    return render(request, template, context)


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

def profile_edit(request):
    template = 'edit_profile.html'
    return render(request, template, context)

# def profile_edit(request):
    # if request.method == 'POST':
    #     form = EditProfileForm(request.POST)
    #     new_user = form.save()
    # return redirect('/Profile')

def success(request):
    return redirect('/profile')

def cancel(request):
    return redirect('/profile')