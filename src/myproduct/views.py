from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductForm
from .models import Product, UserExtendData
from django.contrib.auth.models import User

# Create your views here.
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
                    context = setcontext(form)
                    return render(request, 'product_new.html', context)
            else:
                form = ProductForm()
            context = setcontext(ProductForm())
            return render(request, 'product_new.html', context)


def setcontext(lastform) :
    context = { 'last_name': lastform.data.get('name'),
                'last_type' : lastform.data.get('type'),
                'last_detail' : lastform.data.get('detail'),
                'last_price' : lastform.data.get('price'),
                'last_amount' : lastform.data.get('amount'),
                'last_tags' : lastform.data.get('tags'),
                'form': lastform,
                }
    return  context