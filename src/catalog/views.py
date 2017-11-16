from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

def search(request, product_type, num):
    product_per_page = 18
    real_product_type = ''
    product_name = ''
    seller_name = ''
    sort_type = ''
    search_path = ''
    if product_type != '':
        for choice in PRODUCT_TYPE_CHOICES:
            if choice[0] == product_type:
                real_product_type = choice[1]
    page = int(num)
    if page < 1:
        return redirect('/shop/' + real_product_type)
    first_product = product_per_page * (page - 1)
    last_product = product_per_page * page
    if ('seller_name' in request.GET) and ('product_name' in request.GET) and ('sort' in request.GET):
        product_name = request.GET['product_name']
        seller_name = request.GET['seller_name']
        sort_type = request.GET['sort']
        search_path = '/?product_name=' + product_name + '&seller_name=' + seller_name + '&sort=' + sort_type
        user_list = User.objects.filter(username__icontains=seller_name)
        user_extend_data_list = UserExtendData.objects.filter(user__in=user_list)
        if sort_type == 'low':
            sort_word = 'price'
        elif sort_type == 'high':
            sort_word = '-price'
        elif sort_type == 'old':
            sort_word = 'create_date'
        else:
            sort_word = '-create_date'
        if real_product_type == '':
            all_product = Product.objects.order_by(sort_word).filter(seller__in=user_extend_data_list,
                                                                             name__icontains=product_name)[first_product:last_product]
            all_product_length = Product.objects.filter(seller__in=user_extend_data_list,
                                                        name__icontains=product_name).count()
        else:
            all_product = Product.objects.order_by(sort_word).filter(type=product_type, seller__in=user_extend_data_list,
                                                                             name__icontains=product_name)[first_product:last_product]
            all_product_length = Product.objects.filter(type=product_type, seller__in=user_extend_data_list,
                                                        name__icontains=product_name).count()
    else:
        if real_product_type == '':
            all_product = Product.objects.order_by('-create_date')[first_product:last_product]
            all_product_length = Product.objects.count()
        else:
            all_product = Product.objects.order_by('-create_date').filter(type=product_type)[first_product:last_product]
            all_product_length = Product.objects.filter(type=product_type).count()
    if all_product_length == 0:
        last_page = 0
    else:
        last_page = int(all_product_length / product_per_page)
        if all_product_length % product_per_page != 0:
            last_page += 1
    context = {
        'type': '/' + real_product_type,
        'page': page,
        'last_page': last_page,
        'all_product': all_product,
        'default_product_name': product_name,
        'default_seller_name': seller_name,
        'default_sort_type': sort_type,
        'search_path': search_path,
        'tags': Tag.objects.all(),
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
