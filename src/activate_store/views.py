from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta

from main.models import UserExtendData, TopUp
from .forms import upload_img_form

@login_required
def activate_store(request):
    user = request.user
    user_extend = UserExtendData.objects.get(user_id=user.pk)
    expire_date = user_extend.selling_expire_date
    context = locals()
    if user_extend.first_time():
        user_extend.selling_expire_date = datetime.now()+timedelta(days=30)
        user_extend.free_trial_status = 0;
        user_extend.save()
        template = 'my_store_first_time.html'
        return render(request, template, context)
    else:
        if user_extend.can_sell():
            return redirect('/profiles/shopstatus/')
        else:
            template = 'my_store_expired.html'
            return render(request, template, context)

@login_required
def top_up(request):
    user = request.user
    if request.method == 'POST':
        top_up_form = upload_img_form(request.POST, request.FILES, instance=user)
        if top_up_form.is_valid():
            top_up_form.save()
            return redirect('home')
    else:
        top_up_form = upload_img_form()
    return render(request, 'top_up.html', {'form': top_up_form})
