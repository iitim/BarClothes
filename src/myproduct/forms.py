from django import forms
from django.forms import Textarea, CheckboxSelectMultiple
from .models import Product, PRODUCT_TYPE_CHOICES, Tag

class ProductForm(forms.ModelForm):
    amount = forms.IntegerField(min_value=1)
    price = forms.IntegerField(min_value=0)
    # An inline class to provide additional information on the form.
    class Meta:
        model = Product
        fields = ('name', 'type', 'price', 'amount', 'tags', 'detail', 'picture_path')
        widgets = {'detail': Textarea(attrs={'cols': 110, 'rows': 6}),}
        # 'tags': CheckboxSelectMultiple()}

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'type', 'price', 'amount', 'tags', 'detail', 'picture_path')
        widgets = {'detail': Textarea(attrs={'cols': 110, 'rows': 6}),}