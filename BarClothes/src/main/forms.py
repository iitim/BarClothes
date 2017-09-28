from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import USER_TYPE_CHOICES

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    id_num = forms.CharField(max_length=30)
    phone_num = forms.CharField(max_length=30)
    # dob_num = forms.DateTimeField(required=True)
    type_user = forms.CharField(widget=forms.Select(choices=USER_TYPE_CHOICES))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
