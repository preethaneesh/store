from django.urls import path
from . import views

urlpatterns = [

    path('',views.demo,name='demo'),
    path('login',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('forms',views.forms,name='forms'),
    path('login/new/',views.new,name='new'),
    path('logout',views.logout,name='logout'),
    path('forms/msg/',views.msg,name='msg'),


]