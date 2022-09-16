from django.contrib import admin
from django.urls import path
from users.views import login_request,register,login_request_super,update_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_request,name='login'),
    path('login-super/',login_request_super,name='login-super'),
    path('register/',register,name='register'),
    path('logout/',LogoutView.as_view(template_name="users/logout.html"),name='logout'),
    
    path('update-profile/',update_profile,name='update_profile'),
]