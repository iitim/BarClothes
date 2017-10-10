from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import USER_STATUS_CHOICES

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    id_num = forms.CharField(max_length=30)
    phone_num = forms.CharField(max_length=30)
    # dob_num = forms.DateTimeField(required=True)
    type_user = forms.CharField(widget=forms.Select(choices=USER_STATUS_CHOICES))

    @staticmethod
    def is_valid_nat_id(id_num):
        if len(id_num) != 13:
            return False
        for c in id_num:
            if c >'9' or c <'0':
                return False
        return True

    def clean_national_id(self):
        if not SignUpForm.is_valid_nat_id(self.cleaned_data['id_num']):
            del self.cleaned_data['id_num']
            raise ValidationError('Incorrect Format', code='invalid')

    def clean_password_confirm(self):
        if 'password1' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                del self.cleaned_data['password2']
                raise ValidationError('Password does not match', code='invalid' )
        return self.cleaned_data['password2']

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
