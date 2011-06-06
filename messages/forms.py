from django import forms
from django.contrib.auth.models import User

class MessageForm(forms.Form):
	subject = forms.CharField(max_length=60)
	message = forms.CharField(widget=forms.Textarea)

class PublicMessageForm(forms.Form):
	message = forms.CharField(widget=forms.Textarea,max_length=160)
