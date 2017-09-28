from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

USER_TYPE = (
        ('Customer', 'Customer'),
        ('Seller', 'Seller'),
)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    id_num = forms.CharField(max_length=30)
    phone_num = forms.CharField(max_length=30)
    dob_num = forms.DateTimeField(required=True)
    us_type = forms.Select(choices=USER_TYPE)
    is_seller = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
