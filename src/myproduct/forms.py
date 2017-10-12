from django import forms
from .models import Product, PRODUCT_TYPE_CHOICES

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=45)
    type = forms.ChoiceField(choices=PRODUCT_TYPE_CHOICES)

    # An inline class to provide additional information on the form.
    class Meta:
        model = Product
        fields = ('name', 'type',)