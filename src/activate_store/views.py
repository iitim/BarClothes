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
def wait_page(request):
    context = locals()
    template = 'wait.html'
    return render(request, template, context)

@login_required
def activate_store(request):
    user = request.user
    user_extend = UserExtendData.objects.get(user_id=user.pk)
    expire_date = user_extend.selling_expire_date
    context = locals()
    if user_extend.first_time():
        # if request.method == 'POST':    
        print("POST")    
            # user_extend.selling_expire_date = datetime.now()+timedelta(days=30)
            # user_extend.free_trial_status = 0;
            # user_extend.save()
            # return redirect('/profiles/shopstatus/')
        template = 'my_store_first_time.html'
        return render(request, template, context)
    else:
        if user_extend.can_sell():
            try:
                print('shopstatus')
                top_up = TopUp(user=user)
                if top_up.status == 'S':
                    return redirect('/profiles/shopstatus/')
                else:
                    print('wait1')
                    template = 'wait.html'
                    return render(request, template, context)
            except:
                print('wait2')
                template = 'wait.html'
                return render(request, template, context)
        else:
            print('expired')
            template = 'my_store_expired.html'
            return render(request, template, context)

@login_required
def top_up(request):
    user = request.user
    top_up = TopUp(user=user)
    if request.method == 'POST':
        top_up_form = upload_img_form(request.POST, request.FILES, instance=top_up)
        if top_up_form.is_valid():
            top_up_form.save()
            top_up.user = user
            top_up.price = top_up_form.cleaned_data.get('price')
            top_up.status = 'w'
            top_up.save()
            print(top_up_form)
            return redirect('/activate_store/wait_page')
    else:
        top_up_form = upload_img_form(instance=top_up)
    return render(request, 'top_up.html', {'form': top_up_form})

@login_required
def free_trial(request):
    print("free trial")
    # user = request.user
    # user_extend = UserExtendData.objects.get(user_id=user.pk)
    # user_extend.selling_expire_date = datetime.now()+timedelta(days=30)
    # user_extend.free_trial_status = 0;
    # user_extend.save()
    return redirect('/profiles/shopstatus/')
