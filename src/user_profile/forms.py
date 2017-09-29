from django import forms
from django.forms import ModelForm
from main.models import UserExtendData
from django.contrib.auth.models import User

# Create the form class.
class EditProfileForm(ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    id_num = forms.CharField(max_length=30)
    phone_num = forms.CharField(max_length=30)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'id_num', 'phone_num', 'email']

# Creating a form to add an article.
# form = EditProfileForm()

# Creating a form to change an existing article.
# article = Article.objects.get(pk=1)
# form = ArticleForm(instance=article)