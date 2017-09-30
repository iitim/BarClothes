from django.shortcuts import render
from .models import Product

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

def filter(product_type, num):
    print("parameter num in filter = ", num)
    page = int(num)
    first_product = 18*(page-1)
    if first_product < 0 :
        first_product = 0
    last_product = 18*page
    product = Product.objects.filter(type=product_type).order_by('-create_date')[first_product:last_product]
    product_count = len(product)
    all_full_row = []
    remain_row = []
    for i in range(int(product_count / 3)):
        all_full_row.append(product[i:i + 3])
    for i in range(product_count % 3):
        remain_row = product[product_count - (product_count % 3):product_count]
    context = {
        'type': '/' + product_type,
        'previous_page': page-1,
        'next_page': page+1,
        'all_full_row': all_full_row,
        'remain_row': remain_row
    }
    return context

def catalog(request, num="1"):
    page = int(num)
    first_product = 18 * (page - 1)
    if first_product < 0:
        first_product = 0
    last_product = 18*page
    product = Product.objects.order_by('-create_date')[first_product:last_product]
    product_count = len(product)
    all_full_row = []
    remain_row = []
    for i in range(int(product_count/3)):
        all_full_row.append(product[i:i+3])
    for i in range(product_count%3):
        remain_row = product[product_count-(product_count%3):product_count]
    context = {
        'type': '',
        'previous_page': page-1,
        'next_page': page+1,
        'all_full_row': all_full_row,
        'remain_row': remain_row
    }
    template = 'catalog.html'
    return render(request, template, context)

def top(request, num="1"):
    print(request)
    print("parameter num in top = ", num)
    context = filter('top', num)
    template = 'catalog.html'
    return render(request, template, context)

def jacket(request, num="1"):
    context = filter('jacket', num)
    template = 'catalog.html'
    return render(request, template, context)

def dress(request, num="1"):
    context = filter('dress', num)
    template = 'catalog.html'
    return render(request, template, context)

def skirt(request, num="1"):
    context = filter('skirt', num)
    template = 'catalog.html'
    return render(request, template, context)

def pants(request, num="1"):
    context = filter('pants', num)
    template = 'catalog.html'
    return render(request, template, context)

def shorts(request, num="1"):
    context = filter('shorts', num)
    template = 'catalog.html'
    return render(request, template, context)

def tshirt(request, num="1"):
    context = filter('t-shirt', num)
    template = 'catalog.html'
    return render(request, template, context)

def suits(request, num="1"):
    context = filter('suits', num)
    template = 'catalog.html'
    return render(request, template, context)

def bag(request, num="1"):
    context = filter('bag', num)
    template = 'catalog.html'
    return render(request, template, context)

def shoes(request, num="1"):
    context = filter('shoes', num)
    template = 'catalog.html'
    return render(request, template, context)

def accessory(request, num="1"):
    context = filter('accessory', num)
    template = 'catalog.html'
    return render(request, template, context)