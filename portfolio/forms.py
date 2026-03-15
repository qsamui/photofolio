from django import forms
from .models import Category
class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=120,
                           widget=forms.TextInput(attrs={'placeholder':'Your name'}))
    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(attrs={'placeholder':'Your email'}))
    message = forms.CharField(label="Message",
                              widget=forms.Textarea(attrs={'placeholder':'Your message'}))


