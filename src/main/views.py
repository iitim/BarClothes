from django.shortcuts import render

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)
