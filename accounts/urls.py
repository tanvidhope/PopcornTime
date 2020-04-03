from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
	path('register/', views.registerPage, name='signup'),
	path('login/', views.loginPage, name='signin'),  
	path('logout/', views.logoutUser, name='signout'),
]