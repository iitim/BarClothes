# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from main.models import UserExtendData 
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

def profile_edit(request):
    template = 'edit_profile.html'
    return render(request, template, context)

def success(request):
    context = locals()
    template = 'profile.html'
    return render(request, template, context)