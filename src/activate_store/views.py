from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from main.models import UserExtendData, TopUp
from .forms import top_up_form

@login_required
def activate_store(request):
    user = request.user
    user_extend = UserExtendData.objects.get(user_id=user.pk)
    expire_date = user_extend.expire_date
    context = locals()
    if first_time():
        user_extend.free_trial_status = 0;
        template = 'my_store_first_time.html'
        return render(request, template, context)
    else:
        if can_sell():
            template = 'my_store_expired.html'
            return render(request, template, context)
        else:
            template = 'store.html'
            return render(request, template, context)

@login_required
def top_up(request):
    if request.method == 'POST':
        form = top_up_form(request.POST)
        if form.is_valid():
            form.save()
            slip_pic = form.cleaned_data.get('slip_pic')
            user = request.user
            user_topup = TopUp.objects.get(user_id=user.pk)
            user_topup.slip_pic = slip_pic
            user_topup.save()
            return redirect(reverse("{% url 'store' %}"))
        else:
            print(form.errors)
            return render(request, 'top_up.html', {'form': form})
    else:
        form = top_up_form()
        return render(request, 'top_up.html', {'form': form})
