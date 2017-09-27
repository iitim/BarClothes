from django.shortcuts import render

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

def catalog(request):
    context = locals()
    template = 'catalog.html'
    return render(request, template, context)
