from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Product, PRODUCT_TYPE_CHOICES
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

# from main.forms import SignUpForm
# from main.models import UserExtendData

def home(request):
    product = Product.objects.order_by('-pk')
    num = len(product)
    for i in range(num):
        if not product[i].seller.can_sell() or product[i].remain() == 0:
            temp = product[i].amount
            product[i].amount = 0
            product[i].save()
            # print(product[i])
            # print(product[i].amount)
            product[i].amount = temp
            # print(product[i].amount)
    
    interesting = product.filter(~Q(amount = 0))

    for i in range(num):
        if not product[i].seller.can_sell() or product[i].remain() <= 0:
            product[i].save()
            # print(product[i])
            # print(product[i].amount)

    bestsell = interesting.order_by('-view')
    
    # interesting = Product.objects.order_by('-pk')
    # bestsell = Product.objects.order_by('-view')
    num_product_interesting = len(interesting)
    num_product = len(bestsell)
    template = 'home.html'
    context = {
        'interesting' : interesting,
        'bestsell' : bestsell,
        'num_product' : num_product,
        'num_product_interesting' : num_product_interesting
    }
    return render(request, template, context)

def store(request):
    context = locals()
    template = 'store.html'
    return render(request, template, context)

def login(request):
    context = locals()
    template = 'login.html'
    return render(request, template, context)

def logout(request):
    context = locals()
    template = 'logged_out.html'
    return render(request, template, context)

def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)
    else:
        form = form_class()

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'MESSAGE from barclothes.com'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        return HttpResponseRedirect('/contact/')

    return render(request, 'contact.html', {
        'form': form,  # NOTE: instead of form_class!!!!
    })
