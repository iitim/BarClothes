from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductForm, ProductUpdateForm
from .models import Product, UserExtendData
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
                    return redirect('home')
                else:
                    print(form.data)
            else:
                form = ProductForm()
            return render(request, 'product_new.html', {'last_name': form.data.get('name'), 'form': form,})

def product_update(request, num):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    else:
        user = get_object_or_404(UserExtendData, user=request.user)
        product = get_object_or_404(Product, pk=num)
        if (user.can_sell() == False) or (not user == product.seller):
            return redirect('home')
        else:
            form = ProductUpdateForm(instance=product)
            if request.POST:
                form = ProductUpdateForm(request.POST, request.FILES, instance=product)
                if form.is_valid():
                    form.save()
            return render(request, 'product_update.html', {'form': form, 'product' : product,})

def product_delete(request):
    template = 'product_delete.html'
    context = locals()
    return render(request, template, context)