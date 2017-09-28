from django.shortcuts import render

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

# def profile(request):
# 	context = locals()
# 	template = 'profile.html'
# 	return render(request, template, context)

# def change_password(request):
# 	context = locals()
# 	template = 'changepass.html'
# 	return render(request, template, context)

# def profile_edit(request):
# 	context = locals()
# 	template = 'edit_profile.html'
# 	return render(request, template, context)

# def success(request):
# 	context = locals()
# 	template = 'profile.html'
# 	return render(request, template, context)