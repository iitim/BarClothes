from django.forms import ModelForm, TextInput

from main.models import TopUp

class upload_img_form(ModelForm):
	class Meta:
		model = TopUp
		fields = ['slip_pic', 'price']
