# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from main.models import TransactionLog, Transaction, UserExtendData

from django.shortcuts import render, get_object_or_404

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
    user = get_object_or_404(UserExtendData, user=request.user)
    context = {
        'logs': TransactionLog.objects.order_by('-create_date').filter(customer=user)[0:10],
        'transacts': Transaction.objects.order_by('-create_date').filter(customer=user),
    }
    template = 'transcus.html'
    return render(request, template, context)
