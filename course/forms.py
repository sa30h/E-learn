from django import forms
from .models import *

# from .models import User

class CourseForm(forms.ModelForm):

	class Meta:
		model=course
		fields="__all__"

class CoursecareerForm(forms.ModelForm):

	class Meta:
		model=coursecareer
		fields="__all__"




