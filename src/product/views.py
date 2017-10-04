from django.shortcuts import get_object_or_404, render
from .models import Product

def product_view(request, num):
    product = get_object_or_404(Product, pk=num)
    return render(request, 'product_view.html', {'product': product})
