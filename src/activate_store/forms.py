from django import forms
from django.forms import ModelForm, TextInput

from main.models import TopUp

class upload_img_form(ModelForm):
	class Meta:
		model = TopUp
		fields = ['slip_pic', 'price'] 

	def __init__(self, *args, **kwargs):
		super(upload_img_form, self).__init__(*args, **kwargs)
		self.fields['price'] = forms.IntegerField(
			min_value = 0
		)
