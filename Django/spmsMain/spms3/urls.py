from django.contrib import admin
from django.urls import path, include
from spms3 import views,

urlpatterns = [
    path('', views.login, name='sign-in'),
    path('sign_in', views.login, name='sign-in'),
    path('faculty/dashboard', views.fDashboard, name='faculty-dashboard'),
    path('faculty/co', views.fCo, name='faculty-co'),
    path('faculty/qb', views.fQb, name='faculty-qb'),
    path('student/dashboard', views.sDashboard, name='student-dashboard'),
    path('student/co', views.sCo, name='student-co'),
    path('student/qb', views.sQb, name='student-qb'),
    path('createqb', views.createQb, name='create-qb'),
    path('createco', views.createCo, name='create-co'),
    path('viewassessment', views.viewAssessment, name='view-assessment'),
    path('viewco', views.viewCo, name='view-co'),

]
