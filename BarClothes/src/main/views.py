from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

<<<<<<< HEAD
# <<<<<<< HEAD
# # from main.forms import SignUpForm
# # from main.models import UserExtendData
#
# =======
# >>>>>>> 9e911d7ed4ade2456e6a4afceb9b006322230f57
=======
<<<<<<< HEAD
# from main.forms import SignUpForm
# from main.models import UserExtendData

=======
>>>>>>> 9e911d7ed4ade2456e6a4afceb9b006322230f57
>>>>>>> e93a5bfbdd3da7158d83c65f56a2267bb9c9cb07
def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

def login(request):
    context = locals()
    template = 'login.html'
    return render(request, template, context)

def logout(request):
    context = locals()
    template = 'logged_out.html'
    return render(request, template, context)

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             new_user =  form.save()
#             idnum = form.cleaned_data.get('id_num')
#             phone = form.cleaned_data.get('phone_num')
#             # dob = form.cleaned_data.get('dob_num')
#             type_user = form.cleaned_data.get('type_user')
#             us = UserExtendData(user=new_user, type=type_user, id_num=idnum, tel_no=phone)
#             us.save()
#             if type_user == 'S' :
#                 seller_extend_data = SellerExtendData(user=new_user)
#                 seller_extend_data.save()
#             # username = form.cleaned_data.get('username')
#             # raw_password = form.cleaned_data.get('password1')
#             # user = authenticate(username=username, password=raw_password)
#             # login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'signup.html', {'form': form})
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})
