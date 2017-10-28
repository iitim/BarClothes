from django import forms
from .models import Transaction

class Num_BuyForm(forms.ModelForm):
    amount = forms.IntegerField(min_value=1)
    class Meta:
        model = Transaction
        fields = ('amount',)