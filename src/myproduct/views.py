from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductForm
from .models import Product, UserExtendData
from django.contrib.auth.models import User

# Create your views here.
def product_new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name =  form.cleaned_data.get('name')
            seller = get_object_or_404(UserExtendData, user=request.user)
            type = form.cleaned_data.get('type')
            new_product = Product(name=name, type=type, seller=seller)
            new_product.save()
            
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
                'form': lastform,
                }
    return  context