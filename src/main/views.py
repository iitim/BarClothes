from django.shortcuts import render

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

def profile(request):
	context = locals()
	template = 'profile.html'
	return render(request, template, context)