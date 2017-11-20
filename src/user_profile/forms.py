from django import forms
from django.forms import ModelForm,TextInput,FileInput
from django.contrib.auth.models import User
from main.models import UserExtendData 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from main.models import UserExtendData, Transaction

# Create the form class.
class EditProfileForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=30)
    # last_name = forms.CharField(max_length=30)
    # email = forms.EmailField(max_length=254, )
    # phone_num = forms.CharField(max_length=30)

    first_name = forms.CharField(
        max_length=30,
            widget = forms.TextInput(
                attrs = {
                    'class': 'input-edit-text2', 
                    'type': 'text',
                    'value' : "{{ user.first_name }}"
                }
            )
    )
    last_name = forms.CharField(
        max_length=30,
        widget = forms.TextInput(
            attrs = {
                'class': 'input-edit-text2', 
                'type': 'text',
                'value' : '{{ user.last_name }}'
            }
        )
    )
    email = forms.CharField(
        max_length=254,
        help_text='Required. Inform a valid email address.',
        widget = forms.TextInput(
            attrs = {
                'class': 'input-edit-text4', 
                'type': 'tel',
                'value' : '{{ user.email }}'
            }
        )
    )


    class Meta:
        model = UserExtendData
        # user = get_user_model()
        fields = ('address', 'tel_no', 'picture','bank_account')
        widgets = {
            'address': TextInput(attrs={
                'class': 'input-edit-text-3', 
                'type': 'text',
                # 'value': 'user.first_name'
            }),
            'tel_no': TextInput(attrs={
                'class': 'input-edit-text-1', 
                'type': 'text',
                # 'value': 'user.first_name'
            }),
                        
            'picture': FileInput(attrs={
                'class' : "edit-pic",
                'type' : "file",
                'value' : 'edit_profile_form.picture',
             }),
            
            'bank_account': TextInput(attrs={
                'class': 'input-edit-text-bank', 
                'type': 'text',
                # 'value': 'user.first_name'
            }),
        }

class TransactionUpdateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('transport_code',)
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['picture'] = forms.ImageField(
            required=False
        )
