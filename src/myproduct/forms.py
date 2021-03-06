from django import forms
from django.forms import Textarea, CheckboxSelectMultiple
from .models import Product, PRODUCT_TYPE_CHOICES, Tag

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'type', 'price', 'amount', 'tags', 'detail', 'picture_path')
        widgets = {'detail': Textarea(attrs={'cols': 110, 'rows': 6}),}

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'type', 'price', 'amount', 'tags', 'detail', 'picture_path')
        widgets = {'detail': Textarea(attrs={'cols': 110, 'rows': 6}),}