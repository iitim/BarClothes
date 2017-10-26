from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)
