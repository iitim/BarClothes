from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, UserExtendData, Transaction, TransactionLog, TRANSACTION_STATUS_CHOICES
from django.contrib.auth.models import User
from .forms import UpdateSlipForm
from datetime import datetime, timedelta
from django.utils import timezone

def mycart(request):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    else:
        user = get_object_or_404(UserExtendData, user=request.user)

        updateExpire(request, user)

        transactions = Transaction.objects.order_by('-create_date').filter(customer=user)
        transactions_error = transactions.filter(status='cpe')
        transactions_cart = transactions.filter(status='wpy')
        transactions_check = transactions.filter(status='wac')
        transactions_wait = transactions.filter(status='wss')

        num_transaction_error = len(transactions_error) 
        num_transaction_cart = len(transactions_cart)

        for i in range(num_transaction_error):
            transactions_error[i].slips = updateslipForm(request, transactions_error[i].id)
        for i in range(num_transaction_cart):
            transactions_cart[i].slips = updateslipForm(request, transactions_cart[i].id)

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
        return render(request, 'mycart.html', context)


def updateslipForm(request, num):
    transaction = get_object_or_404(Transaction, pk=num)
    form = UpdateSlipForm(instance=transaction, initial={'pk':transaction._get_pk_val()})
    if request.POST and transaction._get_pk_val() == int(request.POST['pk']):
        if True:
            form = UpdateSlipForm(request.POST, request.FILES, instance=transaction, initial={'pk':transaction._get_pk_val()})
            if form.is_valid():
                # print(form.data)
                # transaction = form.save(commit=False)
                # transaction.expire_date = datetime.now() + timedelta(days=3)
                transaction.payment_picture = form.cleaned_data.get('payment_picture')
                transaction.status = 'wac'
                print(transaction.id)
                print(transaction)
                transaction.save()
                return redirect('user_profile:mycart:mycart')
                # form.save()
    # print("\n")
    return form

def delete(request, num):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login'))
    else:
        user = get_object_or_404(UserExtendData, user=request.user)
        transaction = get_object_or_404(Transaction, pk=num)
        if not transaction.customer == user:
            return redirect('user_profile:mycart:mycart')
        else:
            if transaction.status == 'cpe' or transaction.status == 'wpy':
                transaction.status = 'ccl'
                transaction.save()
                new_transectionLog = TransactionLog.from_transaction(transaction)
                new_transectionLog.save()
                Transaction.objects.filter(pk=num).delete()
            return redirect('user_profile:mycart:mycart')

def updateExpire(request, user):
    transactions = Transaction.objects.filter(customer=user)
    now = timezone.now()
    for transaction in transactions:
        if transaction.expire_date < now and (transaction.status == 'wpy' or transaction.status == 'cpe'):
            transaction.status = 'cnp'
            transaction.save()
            new_transectionLog = TransactionLog.from_transaction(transaction)
            new_transectionLog.save()
            Transaction.objects.filter(pk=transaction.id).delete()