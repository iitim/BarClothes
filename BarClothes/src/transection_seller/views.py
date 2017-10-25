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
    status= {
        'wpy':'unpay',
        'wac':'checking',
        'wss':'waiting',
        'suc':'success',
        'cnp':'not pay',
        'cpe':'payment error',
        'ccl':'cancel',
        'sns':'not sent'
    }
    transacts= Transaction.objects.order_by('-create_date').filter(customer=user)
    for i in range(len(transacts)):
        transacts[i].status = status[transacts[i].status]
    logs= TransactionLog.objects.order_by('-create_date').filter(customer=user)[0:10]
    for i in range(len(logs)):
        logs[i].status = status[logs[i].status]
    context = {
        'logs': logs,
        'transacts': transacts
    }
    template = 'transcus.html'
    return render(request, template, context)
