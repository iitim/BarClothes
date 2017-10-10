# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def mainpage(request):
    context = locals()
    template = 'mainpage.html'
    return render(request, template, context)

def orderpage(request):
    context = locals()
    template = 'delivery_order.html'
    return render(request, template, context)