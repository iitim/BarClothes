from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import Product, PRODUCT_TYPE_CHOICES
from django.contrib.auth.models import User

def product_view(request, num):
    product = get_object_or_404(Product, pk=num)
    type = PRODUCT_TYPE_CHOICES
    product.view += 1
    product.save()
    
    if not request.user.is_authenticated:
        return render(request, 'product_view.html', {'product': product, 'type' : type})
    else:
        user = request.user
        return render(request, 'product_view.html', {'product': product , 'user' : user, 'type' : type})

def product_buy(request, num):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    else:
        product = get_object_or_404(Product, pk=num)
        user = request.user
        if product.remain() > 0:
            product.reserved += 1
            product.save()
            # add Transection buy and Transection sell
            return render(request, 'product_buy.html', {'product': product , 'user' : user})
        else:
            return product_view(request, num)
