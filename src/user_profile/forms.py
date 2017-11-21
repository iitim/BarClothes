from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from main.models import UserExtendData, Transaction

# Create the form class.
class EditProfileForm(forms.ModelForm):
    address = forms.CharField(
        max_length=1000,
            widget = forms.TextInput(
                attrs = {
                    'class': 'input-edit-text-3', 
                    'type': 'text',
                    'value' : "{{ user_extend.address }}"
                }
            )
    )
    tel_no = forms.CharField(
        max_length=45,
        widget = forms.TextInput(
            attrs = {
                'class': 'input-edit-text-1', 
                'type': 'text',
                'value' : '{{ user_extend.tel_no }}'
            }
        )
    )
    id_num = forms.CharField(
        max_length=13,
        widget = forms.TextInput(
            attrs = {
                'class': 'input-edit-text5', 
                'type': 'tel',
                'value' : '{{ user_extend.id_num }}'
            }
        )
    )

    class Meta:
        model = User
        user = get_user_model()
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username': TextInput(attrs= {
                'class': 'input-edit-text-1', 
                'type': 'text',
                # 'placeholder':  user.username
            }),

            'first_name': TextInput(attrs={
                'class': 'input-edit-text2', 
                'type': 'text',
                # 'value': 'user.first_name'
            }),
            'last_name': TextInput(attrs={
                'class': "input-edit-text2", 
                'type': 'text',
            }),
            'email': TextInput(attrs={
                'class': 'input-edit-text4',
                'type': 'email',
            }),
        }

class TransactionUpdateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('status', 'sent_date', 'transport_code')
