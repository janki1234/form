from django.db import models
from django.contrib.auth.models import User

		

class UserProfile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	portfolio=models.URLField(blank=True)
	picture=models.ImageField(upload_to='profile_pics')

	def __str__(self):
		return self.user.username



class BasicData(models.Model):
	name=models.CharField(max_length=245)
	email=models.EmailField()		
	text=models.TextField()

	def __str__(self):
		return self.name