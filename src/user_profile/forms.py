from django import forms
from django.forms import ModelForm
from main.models import UserExtendData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create the form class.
class EditProfileForm(forms.ModelForm):
	address = forms.CharField(max_length=1000)
	tel_no = forms.CharField(max_length=45)
	class Meta:
		model = User
		fields = ['first_name','last_name','email']


# Creating a form to add an article.
# form = EditProfileForm()

# Creating a form to change an existing article.
# article = Article.objects.get(pk=1)
# form = ArticleForm(instance=article)