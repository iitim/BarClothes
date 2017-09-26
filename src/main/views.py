from django.shortcuts import render

def home(request):
    context = locals()
    template = 'home\main.html'
    return render(request, template, context)
