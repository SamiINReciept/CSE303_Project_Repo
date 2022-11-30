from django.contrib import admin
from django.urls import path, include
from spms3 import views

urlpatterns = [
    path('', views.login, name='sign-in'),
    path('sign_in', views.login, name='sign-in'),
    path('faculty/dashboard', views.fDashboard, name='faculty-dashboard'),
    path('faculty/co', views.fCo, name='faculty-co'),
    path('faculty/qb', views.fQb, name='faculty-qb'),
    path('createqb', views.createQb, name='create-qb'),
    path('createco', views.createCo, name='create-co'),

]
