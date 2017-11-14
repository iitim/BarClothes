from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, UserExtendData, Transaction, TransactionLog, TRANSACTION_STATUS_CHOICES
from django.contrib.auth.models import User
from .forms import UpdateSlipForm
from datetime import datetime, timedelta

def mycart(request):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    else:
        user = get_object_or_404(UserExtendData, user=request.user)

        transactions = Transaction.objects.order_by('-create_date').filter(customer=user)
        transactions_error = transactions.filter(status='cpe')
        transactions_cart = transactions.filter(status='wpy')
        transactions_check = transactions.filter(status='wac')
        transactions_wait = transactions.filter(status='wss')

        num_transaction_error = len(transactions_error) 
        num_transaction_cart = len(transactions_cart)

        for i in range(num_transaction_error):
            transactions_error[i].slips = updateslipForm(request, transactions_error[i])
        for i in range(num_transaction_cart):
            transactions_cart[i].slips = updateslipForm(request, transactions_cart[i])

        logs = TransactionLog.objects.order_by('-create_date').filter(customer=user)
        logs_success = logs.filter(status='suc')
        logs_notsent = logs.filter(status='sns')
        logs_notpay = logs.filter(status='cnp')
        logs_cancel = logs.filter(status='ccl')
            
        context = {
                'user': user, 
                'transactions' : transactions,
                'transactions_error' : transactions_error,
                'transactions_cart' : transactions_cart,
                'transactions_check' : transactions_check,
                'transactions_wait' : transactions_wait,
                'logs' : logs,
                'logs_success' : logs_success,
                'logs_notsent' : logs_notsent,
                'logs_notpay' : logs_notpay,
                'logs_cancel' : logs_cancel,
            }
        # if request.POST:
        #     return redirect('user_profile:mycart:mycart')
        return render(request, 'mycart.html', context)


def updateslipForm(request, transaction):
    form = UpdateSlipForm(instance=transaction)
    old_picture = transaction.payment_picture
    if request.POST:
        form = UpdateSlipForm(request.POST, request.FILES, instance=transaction)
        if form.is_valid():
            new_picture = form.cleaned_data.get('payment_picture')
            if not new_picture == old_picture:
                transaction.expire_date = datetime.now()
                transaction.status = 'wac'
                transaction.save()
            form.save()
    return form
        

def delete(request, num):
    transaction = get_object_or_404(Transaction, pk=num)
    if transaction.status == 'cpe' or transaction.status == 'wpy':
        transaction.status = 'ccl'
        transaction.save()
        new_transectionLog = TransactionLog.from_transaction(transaction)
        new_transectionLog.save()
        Transaction.objects.filter(pk=num).delete()
    return redirect('user_profile:mycart:mycart')
