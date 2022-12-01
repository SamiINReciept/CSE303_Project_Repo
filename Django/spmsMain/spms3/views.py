from django.shortcuts import render
#from django.contrib.auth import authenticate, login, logout
#from django.contrib import messages

# Create your views here.

def login(request):
    return render(request, 'signin/sign_in.html')

def fDashboard(request):
    return render(request, 'dashboard/faculty/faculty_dashboard.html')

def fCo(request):
    return render(request, 'dashboard/faculty/faculty_CO.html')

def fQb(request):
    return render(request, 'dashboard/faculty/faculty_QB.html')

def createQb(request):
    return render(request, 'dashboard/faculty/questionbank/createQB.html')

def createCo(request):
    return render(request, 'dashboard/faculty/courseoutline/createCO.html')

def viewAssessment(request):
    return render(request, 'dashboard/faculty/questionbank/viewAssessment.html')

