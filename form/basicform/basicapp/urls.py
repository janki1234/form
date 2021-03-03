from django.urls import path
from .views import register,user_login,index
app_name='basicapp'

urlpatterns=[
	path('',index,name='home_page'),
	path('register/',register,name='register'),
	path('login/$',user_login,name='user_login')
]