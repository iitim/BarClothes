from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from operator import attrgetter
from main.models import UserExtendData, Product
from django.contrib.auth.models import User
from django.db import models


def store(request):
    context = locals()
    return render(request, 'store_catalog.html', context)

def store_detail(request): #num
    store_extend = get_object_or_404(UserExtendData, id_num=65543453)
    store = store_extend.user
    products = store_extend.product_set.all()

    if request.method == 'POST':
        if request.POST['sort'] == 'late' :
            products = sorted(products, key=attrgetter('create_date'), reverse=True)
        elif request.POST['sort'] == 'old' :
            products = sorted(products, key=attrgetter('create_date'))
        elif request.POST['sort'] == 'low':
            products = sorted(products, key=attrgetter('price'))
        else :
            products = sorted(products, key=attrgetter('price'), reverse=True)

    # products_latest = sorted(products, key=attrgetter('create_date'), reverse=True)
    # products_oldest = sorted(products, key=attrgetter('create_date'))
    # products_lowest_price = sorted(products, key=attrgetter('price'))
    # products_highest_price = sorted(products, key=attrgetter('price'), reverse=True)

    context = {
        'store': store,
        'products': products
    }
    return render(request, 'store_detail.html', context)