from django.contrib import admin
from basicapp.models import BasicData,UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(BasicData)