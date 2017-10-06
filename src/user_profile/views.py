# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm,UserCreationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


from main.models import UserExtendData 
from .forms import EditProfileForm

# Create your views here.

@login_required
def profile(request):
    # uncomment 2 lines below for user profile login test
    user = request.user
    user_extend = UserExtendData.objects.get(user_id=user.pk)
    context = {
        'id_num': user_extend.id_num,
        'tel_no': user_extend.tel_no,
        'address': user_extend.address,
    }
    template = 'profile.html'
    return render(request, template, context)

# def change_password(request):
#     context = locals()
#     template = 'changepass.html'
#     return render(request, template, context)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

# @login_required
# def change_password(request):
#     # user = request.user
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change-password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = form.PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', {
#         'form': form
#     })

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # dont logout the user.
            messages.success(request, "Password changed.")
            return redirect("/")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    data = {
        'form': form
    }
    return render(request, "change_password.html", data)

@login_required
def profile_edit(request):
    if request.method == 'POST':
        if 'edit_profile' in request.POST:
            # form = EditProfileForm(request.POST, instance=request.user)
            edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user)
            if edit_profile_form.is_valid():
                edit_profile_form.save()
                tel_no = edit_profile_form.cleaned_data.get('tel_no')
                address = edit_profile_form.cleaned_data.get('address')
                user = request.user
                user_extend = UserExtendData.objects.get(user_id=user.pk)
                user_extend.address = address
                user_extend.tel_no = tel_no
                user_extend.save()
                return redirect(reverse('user_profile:profile'))
            else:
                print(edit_profile_form.errors)
                render(request, 'edit_profile.html', {'edit_profile_form': edit_profile_form})
    else:
        edit_profile_form = EditProfileForm(instance=request.user)
        return render(request, 'edit_profile.html',{'edit_profile_form': edit_profile_form})

def success(request):
    return redirect('/accounts/profile')

def cancel(request):
    return redirect('/accounts/profile')