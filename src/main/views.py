from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Product, PRODUCT_TYPE_CHOICES
from collection.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

# from main.forms import SignUpForm
# from main.models import UserExtendData

def home(request):
    interesting = Product.objects.order_by('-pk')
    bestsell = Product.objects.order_by('-view')
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
    context = locals()
    template = 'contact.html'

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            template =
                get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
