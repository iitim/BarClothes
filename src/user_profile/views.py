# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def profile(request):
    # context คือค่าที่ใช้ในการแสดงผลของ template
    context = locals()
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