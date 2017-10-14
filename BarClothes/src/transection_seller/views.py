# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from main.models import TransactionLog

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

def transcus(request):
    user = request.user
    context = {
        'logs': TransactionLog.objects.order_by('-create_date').filter(customer=user.username)[0:10]
    }
    template = 'transcus.html'
    return render(request, template, context)
