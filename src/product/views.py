from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import Product

def product_view(request, num):
    product = get_object_or_404(Product, pk=num)
    return render(request, 'product_view.html', {'product': product})

def product_buy(request, num):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    product = get_object_or_404(Product, pk=num)
    user = request.user
    return render(request, 'product_buy.html', {'product': product , 'user' : user})