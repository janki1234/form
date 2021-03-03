from django.shortcuts import render
from .forms import UserForm,UserProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from . import forms
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	
	return render(request,'basicapp/index.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('basicapp:home_page'))

def register(request):
	registered=False;
	if request.method == 'POST':
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()

			profile=profile_form.save(commit=False)
			profile.user=user


			if 'picture' in request.FILES:
				profile.picture=request.FILES['picture']
				print(profile.picture)

			profile.save()
			registered=True;
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form=UserForm()
		profile_form=UserProfileForm()

	return render(request,'basicapp/registration.html',
								{'user_form':user_form,
								'profile_form':profile_form,
								'registered':registered})


def user_login(request):

	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('basicapp:home_page'))

			else:
				return HttpResponse('You account is not active')
		else:
			print('Failed!!!!')
			print(username,password)
			return HttpResponse('Invalid username or password')
	else:


		return render(request,'basicapp/login.html')





