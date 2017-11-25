from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm

from main.models import UserExtendData

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user =  form.save()
            idnum = form.cleaned_data.get('id_num')
            phone = form.cleaned_data.get('phone_num')
            # type_user = form.cleaned_data.get('type_user')
            us = UserExtendData(user=new_user, id_num=idnum, tel_no=phone)
            us.save()
            # if type_user == 'S' :
            #     seller_extend_data = SellerExtendData(user=new_user)
            #     seller_extend_data.save()
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
    context = { 'last_username': set_or_space(lastform.data.get('username')),
                'last_first_name': set_or_space(lastform.data.get('first_name')),
                'last_last_name': set_or_space(lastform.data.get('last_name')),
                'last_email': set_or_space(lastform.data.get('email')),
                'last_id_num': set_or_space(lastform.data.get('id_num')),
                'last_phone_num': set_or_space(lastform.data.get('phone_num')),
                'form': lastform,
                }
    return  context

def set_or_space(value) :
    print(value)
    if (value == None) :
        return ''
    return value