from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

def search(request, product_type, num):
    product_per_page = 18
    real_product_type = ''
    if product_type != '':
        for choice in PRODUCT_TYPE_CHOICES:
            if choice[0] == product_type:
                real_product_type = choice[1]
    page = int(num)
    if page < 1:
        return redirect('/shop/' + real_product_type)
    first_product = product_per_page * (page - 1)
    last_product = product_per_page * page
    if request.method == 'POST':
        user_list = User.objects.filter(username__icontains=request.POST['seller_name'])
        user_extend_data_list = UserExtendData.objects.filter(user__in=user_list)
        if real_product_type == '':
            product_latest = Product.objects.order_by('-create_date').filter(seller__in=user_extend_data_list,
                                                                             name__icontains=request.POST['product_name'])[first_product:last_product + 1]
            product_oldest = Product.objects.order_by('create_date').filter(seller__in=user_extend_data_list,
                                                                            name__icontains=request.POST['product_name'])[first_product:last_product + 1]
            product_lowest_price = Product.objects.order_by('price').filter(seller__in=user_extend_data_list,
                                                                            name__icontains=request.POST['product_name'])[first_product:last_product + 1]
            product_highest_price = Product.objects.order_by('-price').filter(seller__in=user_extend_data_list,
                                                                              name__icontains=request.POST['product_name'])[first_product:last_product + 1]
            all_product_length = Product.objects.filter(seller__in=user_extend_data_list,
                                                        name__icontains=request.POST['product_name']).count()
        else:
            product_latest = Product.objects.order_by('-create_date').filter(type=product_type, seller__in=user_extend_data_list,
                                                                             name__icontains=request.POST['product_name'])[first_product:last_product + 1]
            product_oldest = Product.objects.order_by('create_date').filter(type=product_type, seller__in=user_extend_data_list,
                                                                            name__icontains=request.POST['product_name'])[first_product:last_product + 1]
            product_lowest_price = Product.objects.order_by('price').filter(type=product_type, seller__in=user_extend_data_list,
                                                                            name__icontains=request.POST['product_name'])[first_product:last_product + 1]
            product_highest_price = Product.objects.order_by('-price').filter(type=product_type, seller__in=user_extend_data_list,
                                                                              name__icontains=request.POST['product_name'])[first_product:last_product + 1]
            all_product_length = Product.objects.filter(type=product_type, seller__in=user_extend_data_list,
                                                        name__icontains=request.POST['product_name']).count()
    else:
        if real_product_type == '':
            product_latest = Product.objects.order_by('-create_date')[first_product:last_product + 1]
            product_oldest = Product.objects.order_by('create_date')[first_product:last_product + 1]
            product_lowest_price = Product.objects.order_by('price')[first_product:last_product + 1]
            product_highest_price = Product.objects.order_by('-price')[first_product:last_product + 1]
            all_product_length = Product.objects.count()
        else:
            product_latest = Product.objects.order_by('-create_date').filter(type=product_type)[first_product:last_product + 1]
            product_oldest = Product.objects.order_by('create_date').filter(type=product_type)[first_product:last_product + 1]
            product_lowest_price = Product.objects.order_by('price').filter(type=product_type)[first_product:last_product + 1]
            product_highest_price = Product.objects.order_by('-price').filter(type=product_type)[first_product:last_product + 1]
            all_product_length = Product.objects.filter(type=product_type).count()
    if all_product_length == 0:
        last_page = 0
    else:
        last_page = all_product_length / product_per_page
        if all_product_length % product_per_page != 0:
            last_page += 1
    product_latest = product_latest[0:product_per_page]
    product_oldest = product_oldest[0:product_per_page]
    product_lowest_price = product_lowest_price[0:product_per_page]
    product_highest_price = product_highest_price[0:product_per_page]
    context = {
        'type': '/' + real_product_type,
        'page': page,
        'last_page': last_page,
        'product_latest': product_latest,
        'product_oldest': product_oldest,
        'product_lowest_price': product_lowest_price,
        'product_highest_price': product_highest_price,
    }
    if real_product_type == '':
        context['type'] = ''
    return render(request, 'catalog.html', context)

def catalog(request, num='1'):
    return search(request, '', num)

def top(request, num='1'):
    return search(request, 'Top', num)

def jacket(request, num='1'):
    return search(request, 'Jac', num)

def dress(request, num='1'):
    return search(request, 'Dre', num)

def skirt(request, num='1'):
    return search(request, 'Ski', num)

def pants(request, num='1'):
    return search(request, 'Pan', num)

def shorts(request, num='1'):
    return search(request, 'Sht', num)

def tshirt(request, num='1'):
    return search(request, 'T-s', num)

def suits(request, num='1'):
    return search(request, 'Sui', num)

def bag(request, num='1'):
    return search(request, 'Bag', num)

def shoes(request, num='1'):
    return search(request, 'Sho', num)

def accessory(request, num='1'):
    return search(request, 'Acc', num)
