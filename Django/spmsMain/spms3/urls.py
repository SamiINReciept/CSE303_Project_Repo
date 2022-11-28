from django.contrib import admin
from django.urls import path, include
from spms3 import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signin', views.login, name='sign-in')
]
