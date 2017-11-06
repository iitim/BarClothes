from django import forms
from django.forms import Textarea, CheckboxSelectMultiple
from main.models import Transaction
from django.forms.formsets import BaseFormSet

class TransactionSlipForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('payment_picture',)

# class TransactionSlipFormSet(BaseFormSet):
#     def clean(self):
#         if '1' in self.data:
