from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import Product, PRODUCT_TYPE_CHOICES, Transaction, UserExtendData
from .forms import Num_BuyForm
from django.contrib.auth.models import User

def product_view(request, num):
    product = get_object_or_404(Product, pk=num)
    type = PRODUCT_TYPE_CHOICES
    product.view += 1
    if not request.user.is_authenticated:
        product.save()
        if request.method == 'POST':
            return product_buy(request, num, 1)
        else:
            return render(request, 'product_view.html', {'product': product, 'type' : type})
    else:
        user = get_object_or_404(UserExtendData, user=request.user)
        if not user == product.seller :
            product.save()
        if request.method == 'POST':
            form = Num_BuyForm(request.POST)
            if form.is_valid():
                num_buy = form.cleaned_data.get('amount')
            return product_buy(request, num, num_buy)
        else:
            form = Num_BuyForm()
            return render(request, 'product_view.html', 
            {'product': product , 'user' : user, 'type' : type, 'form' : form})

def product_buy(request, num, num_buy):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    else:
        product = get_object_or_404(Product, pk=num)
        user = get_object_or_404(UserExtendData, user=request.user)
        if product.remain() > (float(num_buy) - 1):
            product.reserved += num_buy
            product.save()
            # add Transection
            total_price = float(num_buy) * float(product.price)
            new_transaction = Transaction(customer=user, product=product, amount=num_buy, total_price=total_price)
            new_transaction.save()
            return redirect('%s' % ('user_profile:mycart:mycart'))
        else:
            return product_view(request, num)
