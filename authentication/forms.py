import imp
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# from .models import User

class RegistratinForm(UserCreationForm):

	class Meta:
		model=User
		fields=["username"]




class UserLoginForm(forms.ModelForm):

	class Meta:
		model=User
		fields=['username','password']

	def clean(self):
		if self.is_valid():
			username=self.cleaned_data['username']
			password=self.cleaned_data['password']
			if not authenticate(username=username,password=password):
				raise forms.ValidationError("Invalid Creadentials")
