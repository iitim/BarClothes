from django import forms
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import USER_TYPE_CHOICES
=======
>>>>>>> master

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)
