from django import forms
from .models import BasicData,UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model=User
		fields=('username','email','password')

class UserProfileForm(forms.ModelForm):
	portfolio=forms.URLField(required=False)
	picture = forms.ImageField(required=False)

	class Meta():
		model=UserProfile
		fields=('portfolio','picture')

class BasicForm(forms.ModelForm):
	class Meta():
		model = BasicData
		fields = '__all__'

















# from django.core import validators



# class FormName(forms.Form):
# 	name=forms.CharField()
# 	email=forms.EmailField()
# 	verifyemail=forms.EmailField(label='enter email')
# 	text=forms.CharField(widget=forms.Textarea)
	
# 	def clean(self):
# 		all_clean_data=super().clean()
# 		email=all_clean_data['email']
# 		verify_email=all_clean_data['verifyemail']

# 		if email != verify_email:
# 			raise forms.ValidationError("Didn't matched email")