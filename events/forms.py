from django import forms
from django.contrib.auth.models import User

class EventForm(forms.Form):
	game_master = forms.CharField(max_length=10)
	# user_role = forms.CharField(max_length=10)
	slots = forms.IntegerField()
	location = forms.CharField(max_length=20)
