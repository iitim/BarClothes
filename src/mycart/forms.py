from django import forms
# from django.forms import Textarea, CheckboxSelectMultiple
from .models import Transaction

class UpdateSlipForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('payment_picture',)
        # widgets = {'detail': Textarea(attrs={'cols': 110, 'rows': 6}),}