from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, UserExtendData, Transaction, TransactionLog, TRANSACTION_STATUS_CHOICES
from django.contrib.auth.models import User

def mycart(request):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    else:
        user = get_object_or_404(UserExtendData, user=request.user)
        context = {
            'user': user, 
            }
        # context = locals()
        return render(request, 'mycart.html', context)
