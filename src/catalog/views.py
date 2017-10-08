from django.shortcuts import render
from .models import Product

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

def filter(product_type, num):
    page = int(num)
    first_product = 18*(page-1)
    if first_product < 0 :
        first_product = 0
    last_product = 18*page
    product = Product.objects.filter(type=product_type).order_by('-create_date')[first_product:last_product]
    context = {
        'type': '/' + product_type,
        'previous_page': page-1,
        'next_page': page+1,
        'all_product': product
    }
    return context

def catalog(request, num="1"):
    page = int(num)
    first_product = 18 * (page - 1)
    if first_product < 0:
        first_product = 0
    last_product = 18*page
    product = Product.objects.order_by('-create_date')[first_product:last_product]
    context = {
        'type': '',
        'previous_page': page-1,
        'next_page': page+1,
        'all_product': product
    }
    template = 'catalog.html'
    return render(request, template, context)

def top(request, num="1"):
    context = filter('Top', num)
    template = 'catalog.html'
    return render(request, template, context)

def jacket(request, num="1"):
    context = filter('Jac', num)
    template = 'catalog.html'
    return render(request, template, context)

def dress(request, num="1"):
    context = filter('Dre', num)
    template = 'catalog.html'
    return render(request, template, context)

def skirt(request, num="1"):
    context = filter('Ski', num)
    template = 'catalog.html'
    return render(request, template, context)

def pants(request, num="1"):
    context = filter('Pan', num)
    template = 'catalog.html'
    return render(request, template, context)

def shorts(request, num="1"):
    context = filter('Sht', num)
    template = 'catalog.html'
    return render(request, template, context)

def tshirt(request, num="1"):
    context = filter('T-s', num)
    template = 'catalog.html'
    return render(request, template, context)

def suits(request, num="1"):
    context = filter('Sui', num)
    template = 'catalog.html'
    return render(request, template, context)

def bag(request, num="1"):
    context = filter('Bag', num)
    template = 'catalog.html'
    return render(request, template, context)

def shoes(request, num="1"):
    context = filter('Sho', num)
    template = 'catalog.html'
    return render(request, template, context)

def accessory(request, num="1"):
    context = filter('Acc', num)
    template = 'catalog.html'
    return render(request, template, context)