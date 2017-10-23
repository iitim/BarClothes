from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductForm, ProductUpdateForm
from .models import Product, UserExtendData, Transaction, TransactionLog
from django.contrib.auth.models import User

def product_new(request):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    else:
        seller = get_object_or_404(UserExtendData, user=request.user)
        if seller.can_sell() == False:
            return redirect('home')
        else:
            if request.method == 'POST':
                form = ProductForm(request.POST, request.FILES)
                if form.is_valid():
                    tags = form.cleaned_data.get('tags')
                    new_product = form.save(commit=False)
                    new_product.seller = seller
                    new_product.save()
                    form.save_m2m()
                    return redirect('home') # go to store
                else:
                    print(form.data)
            else:
                form = ProductForm()
            return render(request, 'myproduct_new.html', {'last_name': form.data.get('name'), 'form': form,})

def product_update(request, num):
    if not request.user.is_authenticated:
        return redirect('product:view', num)
    else:
        user = get_object_or_404(UserExtendData, user=request.user)
        product = get_object_or_404(Product, pk=num)
        if (user.can_sell() == False) or (not user == product.seller):
            return redirect('product:view', num)
        else:
            form = ProductUpdateForm(instance=product)
            if request.POST:
                form = ProductUpdateForm(request.POST, request.FILES, instance=product)
                if form.is_valid():
                    form.save()
            return render(request, 'myproduct_update.html', {'form': form, 'product' : product,})

def product_delete(request, num):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    else:
        user = get_object_or_404(UserExtendData, user=request.user)
        product = get_object_or_404(Product, pk=num)
        if (user.can_sell() == False) or (not user == product.seller):
            return redirect('product:view', num)
        else:
            form = ProductUpdateForm(instance=product)
            transactions = Transaction.objects.filter(product__id=product.id)
            if request.POST:
                for transaction in transactions:
                    new_transectionLog = TransactionLog.from_transaction(transaction)
                    new_transectionLog.save()
                Transaction.objects.filter(product__id=product.id).delete()
                Product.objects.filter(pk=num).delete()
                return redirect('home')
            return render(request, 'myproduct_delete.html', {'form': form, 'product' : product, 'transections' : transactions})