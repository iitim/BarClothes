from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from main.forms import SignUpForm
# <<<<<<< HEAD
from main.models import UserExtendData, SellerExtendData
# =======
from main.models import UserExtendData,SellerExtendData
# >>>>>>> 9e911d7ed4ade2456e6a4afceb9b006322230f57

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
            # dob = form.cleaned_data.get('dob_num')
            type_user = form.cleaned_data.get('type_user')
            us = UserExtendData(user=new_user, type=type_user, id_num=idnum, tel_no=phone)
            us.save()
            if type_user == 'S' :
                seller_extend_data = SellerExtendData(user=new_user)
                seller_extend_data.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('home')
        else:
            print(form.error_messages)
            print(form.data)
            context = setcontext(form)
            return render(request, 'signup.html', context)
    else:
        form = SignUpForm()
    context = setcontext(SignUpForm())
    return render(request, 'signup.html', context)


def setcontext(lastform) :
    context = { 'last_username':lastform.data.get('username'),
                'last_first_name': lastform.data.get('first_name'),
                'last_last_name': lastform.data.get('last_name'),
                'last_email': lastform.data.get('email'),
                'last_id_num': lastform.data.get('id_num'),
                'last_phone_num': lastform.data.get('phone_num'),
                'form': lastform,
                }
    return  context
