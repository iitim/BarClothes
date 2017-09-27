from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

def catalog(request):
    context = locals()
    template = 'catalog.html'
    return render(request, template, context)
