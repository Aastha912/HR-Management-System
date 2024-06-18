from django.contrib import admin
from django.urls import path ,include
from django.contrib.auth.views import LogoutView
from TYApp import views
urlpatterns = [
    path('', views.index, name='TYApp'),
    path('index', views.index, name='index'),
    path('login', views.loginPage, name='login'),
    path('registration', views.registration, name='registration'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('organisation', views.organisationPage, name='organisation'), 
    path('employee', views.employee, name='employee'),
    path('settings', views.settings, name='settings'),
    path('user', views.userPage, name='user'),
    path('company', views.company, name='company'),
    path('resume_match', views.resume_match, name='resume_match'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
