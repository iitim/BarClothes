from django import forms

from main.models import UserExtendData

class top_up_form(forms.Form):
	slip_pic = forms.ImageField()
