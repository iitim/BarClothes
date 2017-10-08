from django.shortcuts import render , redirect
from .models import Product

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

def filter(product_type, num):
    page = int(num)
    if page < 1 :
        return -1
    first_product = 18*(page-1)
    last_product = 18*page
    is_last_page = False
    product = Product.objects.filter(type=product_type).order_by('-create_date')[first_product:last_product]
    if Product.objects.filter(type=product_type).order_by('-create_date')[last_product:last_product+1] == None :
        is_last_page = True
    context = {
        'type': '/' + product_type,
        'previous_page': page-1,
        'next_page': page+1,
        'is_last_page': is_last_page,
        'all_product': product
    }
    return context

def catalog(request, num="1"):
    print(request.POST)
    if request.method == 'POST' :
        pass
    page = int(num)
    if page < 1 :
        return redirect('/shop')
    first_product = 18 * (page - 1)
    last_product = 18*page
    is_last_page = False
    product = Product.objects.order_by('-create_date')[first_product:last_product]
    if Product.objects.order_by('-create_date')[last_product:last_product+1] == None :
        is_last_page = True
    context = {
        'type': '',
        'previous_page': page-1,
        'next_page': page+1,
        'is_last_page': is_last_page,
        'all_product': product
    }
    template = 'catalog.html'
    return render(request, template, context)

def top(request, num="1"):
    context = filter('Top', num)
    if context == -1 :
        return redirect('/shop/top')
    template = 'catalog.html'
    return render(request, template, context)

def jacket(request, num="1"):
    context = filter('Jac', num)
    if context == -1 :
        return redirect('/shop/jacket')
    template = 'catalog.html'
    return render(request, template, context)

def dress(request, num="1"):
    context = filter('Dre', num)
    if context == -1 :
        return redirect('/shop/dress')
    template = 'catalog.html'
    return render(request, template, context)

def skirt(request, num="1"):
    context = filter('Ski', num)
    if context == -1 :
        return redirect('/shop/skirt')
    template = 'catalog.html'
    return render(request, template, context)

def pants(request, num="1"):
    context = filter('Pan', num)
    if context == -1 :
        return redirect('/shop/pants')
    template = 'catalog.html'
    return render(request, template, context)

def shorts(request, num="1"):
    context = filter('Sht', num)
    if context == -1 :
        return redirect('/shop/shorts')
    template = 'catalog.html'
    return render(request, template, context)

def tshirt(request, num="1"):
    context = filter('T-s', num)
    if context == -1 :
        return redirect('/shop/tshirt')
    template = 'catalog.html'
    return render(request, template, context)

def suits(request, num="1"):
    context = filter('Sui', num)
    if context == -1 :
        return redirect('/shop/suits')
    template = 'catalog.html'
    return render(request, template, context)

def bag(request, num="1"):
    context = filter('Bag', num)
    if context == -1 :
        return redirect('/shop/bag')
    template = 'catalog.html'
    return render(request, template, context)

def shoes(request, num="1"):
    context = filter('Sho', num)
    if context == -1 :
        return redirect('/shop/shoes')
    template = 'catalog.html'
    return render(request, template, context)

def accessory(request, num="1"):
    context = filter('Acc', num)
    if context == -1 :
        return redirect('/shop/accessory')
    template = 'catalog.html'
    return render(request, template, context)