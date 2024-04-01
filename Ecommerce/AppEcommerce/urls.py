from django.contrib.auth.views import LoginView
from django.urls import path
from .views import homePage, user_login, logout_user, user_signup

urlpatterns = [
    path('', homePage, name='home'),
    path('login', user_login, name='login'),
    path('logout', logout_user, name='logout'),
    path('signup', user_signup, name='signup'),

]
