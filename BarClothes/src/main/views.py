from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from main.forms import SignUpForm
from main.models import UserExtendData

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

def login(request):
    context = locals()
    template = 'login.html'
    return render(request, template, context)

def logout(request):
    context = locals()
    template = 'logged_out.html'
    return render(request, template, context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user =  form.save()
            idnum = form.cleaned_data.get('id_num')
            phone = form.cleaned_data.get('phone_num')
            dob = form.cleaned_data.get('dob_num')
            # if request.POST["is_seller"]:
            #     usertype = "S"
            # else:
            #     usertype = "C"
            us = UserExtendData(user=new_user, type=usertype, id_num=idnum, tel_no=phone)
            us.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
