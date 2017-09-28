# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from main.models import UserExtendData 
# Create your views here.
# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
# user.last_name = 'Lennon'

# class UserExtendData(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     type =  models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
#     id_num = models.CharField(max_length=13)
#     address = models.CharField(max_length=100)
#     tel_no = models.CharField(max_length=45)

# context = {
#     'id_num': 'id',
#     'tel_no': '098765',
#     'address': 'UserExtendData.address',
# }

# context = {
#     'id_num': UserExtendData.id_num,
#     'tel_no': UserExtendData.tel_no,
#     'address': UserExtendData.address,
# # }
# @login_required
def profile(request):
    # context คือค่าที่ใช้ในการแสดงผลของ template
    # user = request.user,
    # context.update({'user':user})
    # login(request, user)
    context = {
        # 'user':user,
        'id_num': 'id',
        'tel_no': '098765',
        'address': 'UserExtendData.address',
    }
    print context['tel_no']
    template = 'profile.html'
    return render(request, template, context)

def change_password(request):
    context = locals()
    template = 'changepass.html'
    return render(request, template, context)

def profile_edit(request):
    context = locals()
    template = 'edit_profile.html'
    return render(request, template, context)

def success(request):
    context = locals()
    template = 'profile.html'
    return render(request, template, context)