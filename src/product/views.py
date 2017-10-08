from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import Product, UserExtendData
from django.contrib.auth.models import User

def product_view(request, num):
    product = get_object_or_404(Product, pk=num)
    
    if not request.user.is_authenticated:
        return render(request, 'product_view.html', {'product': product})
    else:
        user = get_object_or_404(UserExtendData, user=request.user)
        return render(request, 'product_view.html', {'product': product , 'user' : user})

def product_buy(request, num):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    else:
        product = get_object_or_404(Product, pk=num)
        user = request.user
        if product.amount > 0:
            product.amount -= 1
            product.save()
            # add Transection buy and Transection sell
            return render(request, 'product_buy.html', {'product': product , 'user' : user})
        else:
            return product_view(request, num)