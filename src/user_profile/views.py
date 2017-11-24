from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from operator import attrgetter
from collections import defaultdict
from datetime import datetime

from .forms import EditProfileForm, TransactionUpdateForm
from main.models import UserExtendData , Transaction, PRODUCT_TYPE_CHOICES


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

def change_password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, data=request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            update_session_auth_hash(request, password_change_form.user) # dont logout the user.
            messages.success(request, "Password changed.")
            return redirect("/")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        password_change_form = PasswordChangeForm(request.user)
    data = {
        'password_change_form': password_change_form
    }
    return render(request, "change_password.html", data)

@login_required
def profile(request):
    user = request.user
    user_extend = UserExtendData.objects.get(user_id=user.pk)

    selling_expire_date = '0'
    if user_extend.free_trial_status == 0:
        selling_expire_date = datetime_string(user_extend.selling_expire_date)
    print(selling_expire_date)

    initial_data = {
        'tel_no' : user_extend.tel_no,
        'address' : user_extend.address,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'email' : user.email,
        'bank_account' : user_extend.bank_account,
    }
    edit_profile_form = EditProfileForm(instance=user_extend, initial=initial_data)
    # edit_profile_form = EditProfileForm(instance=user_extend)
    
    if request.method == 'POST':
        # print('eeieieie')
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=user_extend, initial=initial_data)
        if edit_profile_form.is_valid():
            post = edit_profile_form.save()
            tel_no = edit_profile_form.cleaned_data.get('tel_no')
            address = edit_profile_form.cleaned_data.get('address')
            bank_account = edit_profile_form.cleaned_data.get('bank_account')
            first_name = edit_profile_form.cleaned_data.get('first_name')
            last_name = edit_profile_form.cleaned_data.get('last_name')
            user_extend.address = address
            user_extend.tel_no = tel_no
            user.first_name = first_name
            user.last_name = last_name
            user_extend.bank_account = bank_account
            user.save()
            user_extend.save()
            edit_profile_form.save()
            # print(user.first_name)
            return redirect(reverse('user_profile:profile'))
        else:
            print(edit_profile_form.errors)

    context = {
        'user' : user,
        'edit_profile_form': edit_profile_form,
        'user_extend' : user_extend,
        'selling_expire_date' : selling_expire_date,
    }
    return render(request, 'profile.html', context)

def success(request):
    return redirect('/')

def cancel(request):
    return redirect('/accounts/profile')

def view_myshop(request):
    store_extend = get_object_or_404(UserExtendData, user=request.user)
    if not store_extend.can_sell():
        return redirect('activate_store') #top up
    store = store_extend.user
    type = PRODUCT_TYPE_CHOICES
    products = store_extend.product_set.all()
    products_lowest_price = sorted(products, key=attrgetter('price'))
    context = {
       'products_lowest_price': products_lowest_price,
       'type' : type,
    }
    template = 'mainpage.html'
    return render(request, template, context)
   

def orderpage(request):
    store_extend = get_object_or_404(UserExtendData, user=request.user)
    transaction = Transaction.objects.filter(product__seller=store_extend, status='wss')
    groups = defaultdict(list)
    for obj in transaction:
        groups[obj.product].append(obj)
    new_list = list(groups.values())
    context = {
       'transaction': new_list
    }
    template = 'delivery_order.html'
    return render(request, template, context)

def orderpage_selected(request, num):
    store_extend = get_object_or_404(UserExtendData, user=request.user)
    transaction = Transaction.objects.filter(product__seller=store_extend, status='wss')
    groups = defaultdict(list)
    for obj in transaction:
        groups[obj.product].append(obj)
    new_list = list(groups.values())

    target = get_object_or_404(Transaction, pk=num)
    if target.status != 'wss':
        return redirect('/profiles/shopstatus/order')
    form = TransactionUpdateForm(instance=target)
    if request.POST:
        form = TransactionUpdateForm(request.POST, request.FILES, instance=target)
        print ("form")
        if form.is_valid():
            print ("1")
            fixform = form.save(commit=False)
            fixform.status = 'suc'
            fixform.sent_date = datetime.now()
            form.save()
            return redirect('/profiles/shopstatus/order')

    context = {
       'transaction': new_list,
       'target': target,
       'form': form
    }
    template = 'delivery_order.html'
    return render(request, template, context)

def sentorder(request, transaction):
    form = TransactionUpdateForm(instance=transaction)
    if request.POST:
        form = TransactionUpdateForm(request.POST, request.FILES, instance=transaction)
        if form.is_valid():
            form.save()
    return form

def datetime_string(date_time):
    date = date_time.date().strftime("%d/%m/%y")
    return date