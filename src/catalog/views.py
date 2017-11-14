from django.shortcuts import render , redirect ,get_object_or_404 
from django.contrib.auth.models import User
from .models import *
from operator import attrgetter

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

def filter(request, product_type, num):
    page = int(num)
    if page < 1 :
        return -1
    first_product = 18*(page-1)
    last_product = 18*page
    is_last_page = False
    if request.method == 'POST':
        user_list = User.objects.filter(username__icontains=request.POST['seller_name'])
        user_extend_data_list = UserExtendData.objects.filter(user__in=user_list)
        if request.POST['sort'] == 'late' :
            product = Product.objects.order_by('-create_date')
        elif request.POST['sort'] == 'old' :
            product = Product.objects.order_by('create_date')
        elif request.POST['sort'] == 'low':
            product = Product.objects.order_by('price')
        else :
            product = Product.objects.order_by('-price')
        product = product.filter(type=product_type, seller__in=user_extend_data_list, name__icontains=request.POST['product_name'])[first_product:last_product+1]
        all_product_length = product.filter(type=product_type, seller__in=user_extend_data_list, name__icontains=request.POST['product_name']).count()
    else :
        product = Product.objects.order_by('-create_date').filter(type=product_type)[first_product:last_product+1]
        all_product_length = Product.objects.order_by('-create_date').filter(type=product_type).count()
    if all_product_length == 0 :
         last_page = 0
    else :
         last_page = all_product_length/18 + 1
    if len(product) < 19 :
        is_last_page = True      
    product = product[0:18]
    for choice in PRODUCT_TYPE_CHOICES :
         if choice[0] == product_type :
             real_product_type = choice[1]
    print(real_product_type)
    print(PRODUCT_TYPE_CHOICES[0][1])

    context = {
        'type': '/' + product_type,
        'previous_page': page-1,
        'next_page': page+1,
        'is_last_page': is_last_page,
        'type': '/' + real_product_type,
        'page': page,
        'last_page': last_page,
        'all_product': product,
       
    }
    return context

def catalog(request, num="1"):
    page = int(num)
    if page < 1 :
        return redirect('/shop')
    first_product = 18 * (page - 1)
    last_product = 18*page
    is_last_page = False
    if request.method == 'POST':
        print(request.POST)
        user_list = User.objects.filter(username__icontains=request.POST['seller_name'])
        user_extend_data_list = UserExtendData.objects.filter(user__in=user_list)
        if request.POST['sort'] == 'late' :
            product = Product.objects.order_by('-create_date')
        elif request.POST['sort'] == 'old' :
            product = Product.objects.order_by('create_date')
        elif request.POST['sort'] == 'low':
            product = Product.objects.order_by('price')
        else :
            product = Product.objects.order_by('-price')
        product = product.filter(seller__in=user_extend_data_list, name__icontains=request.POST['product_name'])[first_product:last_product+1]
        all_product_length = product.filter(seller__in=user_extend_data_list, name__icontains=request.POST['product_name']).count()
    else :
        product = Product.objects.order_by('-create_date')[first_product:last_product+1]
        all_product_length = Product.objects.order_by('-create_date').count()
    if all_product_length == 0 :
         last_page = 0
    else :
         last_page = all_product_length/18 + 1
    if len(product) < 19 :
        is_last_page = True

    product = product[0:18]
     # //add
    product_all_latest = Product.objects.order_by('-create_date')
    product_all_oldest = Product.objects.order_by('create_date')
    product_all_lowest_price = Product.objects.order_by('price')
    product_all_highest_price = Product.objects.order_by('-price')

    # add
    context = {
        'type': '',
        'all_product': product,
        'page': page,
        'last_page': last_page,
        'product_latest' : product_all_latest ,
        'product_oldest' : product_all_oldest,
        'product_lowest_price' : product_all_lowest_price,
        'product_highest_price' : product_all_highest_price,
    }
    template = 'catalog.html'
    return render(request, template, context)

def top(request, num="1"):
    context = filter(request, 'Top', num)
    if context == -1 :
        return redirect('/shop/top')
    template = 'catalog.html'
    return render(request, template, context)

def jacket(request, num="1"):
    context = filter(request, 'Jac', num)
    if context == -1 :
        return redirect('/shop/jacket')
    template = 'catalog.html'
    return render(request, template, context)

def dress(request, num="1"):
    context = filter(request, 'Dre', num)
    if context == -1 :
        return redirect('/shop/dress')
    template = 'catalog.html'
    return render(request, template, context)

def skirt(request, num="1"):
    context = filter(request, 'Ski', num)
    if context == -1 :
        return redirect('/shop/skirt')
    template = 'catalog.html'
    return render(request, template, context)

def pants(request, num="1"):
    context = filter(request, 'Pan', num)
    if context == -1 :
        return redirect('/shop/pants')
    template = 'catalog.html'
    return render(request, template, context)

def shorts(request, num="1"):
    context = filter(request, 'Sht', num)
    if context == -1 :
        return redirect('/shop/shorts')
    template = 'catalog.html'
    return render(request, template, context)

def tshirt(request, num="1"):
    context = filter(request, 'T-s', num)
    if context == -1 :
        return redirect('/shop/tshirt')
    template = 'catalog.html'
    return render(request, template, context)

def suits(request, num="1"):
    context = filter(request, 'Sui', num)
    if context == -1 :
        return redirect('/shop/suits')
    template = 'catalog.html'
    return render(request, template, context)

def bag(request, num="1"):
    context = filter(request, 'Bag', num)
    if context == -1 :
        return redirect('/shop/bag')
    template = 'catalog.html'
    return render(request, template, context)

def shoes(request, num="1"):
    context = filter(request, 'Sho', num)
    if context == -1 :
        return redirect('/shop/shoes')
    template = 'catalog.html'
    return render(request, template, context)

def accessory(request, num="1"):
    context = filter(request, 'Acc', num)
    if context == -1 :
        return redirect('/shop/accessory')
    template = 'catalog.html'
    return render(request, template, context)
