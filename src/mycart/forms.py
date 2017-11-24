from django import forms
# from django.forms import Textarea, CheckboxSelectMultiple, ModelForm, TextInput
from .models import Transaction
from django.forms import HiddenInput

class UpdateSlipForm(forms.ModelForm):
    pk = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Transaction
        fields = ('payment_picture',)
        # widgets = {'detail': Textarea(attrs={'cols': 110, 'rows': 6}),}