from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Product

# from main.forms import SignUpForm
# from main.models import UserExtendData

def home(request):
    interesting = Product.objects.order_by('pk')[0:9]
    bestsell = Product.objects.order_by('-pk')[0:9]
    template = 'home.html'
    return render(request, template, {'interesting' : interesting, 'bestsell' : bestsell})

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
    context = locals()
    template = 'contact.html'
    return render(request, template, context)