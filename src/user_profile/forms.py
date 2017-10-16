from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from main.models import UserExtendData

# Create the form class.
class EditProfileForm(forms.ModelForm):
	address = forms.CharField(max_length=1000)
	tel_no = forms.CharField(max_length=45)
	class Meta:
		model = User
		fields = ['first_name','last_name','email']

class top_up_form(forms.Form):
	slip_pic = forms.ImageField()

# Creating a form to add an article.
# form = EditProfileForm()

# Creating a form to change an existing article.
# article = Article.objects.get(pk=1)
# form = ArticleForm(instance=article)
