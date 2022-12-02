from django.shortcuts import render
#from django.contrib.auth import authenticate, login, logout
#from django.contrib import messages
from spms3.models import SCHOOL_T

# Create your views here.

def show_object(request):
    display_school= SCHOOL_T.objects.all()
    return render(request,'dashboard/faculty/courseoutline/createCO.html',{'SCHOOL_T':display_school})

def login(request):
    if request.method == 'POST':
        utype = (request.POST.get('usertype'))
        if utype == "faculty":
            return render(request, 'dashboard/faculty/faculty_dashboard.html')
        else:
            return render(request, 'dashboard/student/student_dashboard.html')

    return render(request, 'signin/sign_in.html')

def fDashboard(request):
    return render(request, 'dashboard/faculty/faculty_dashboard.html')

def fCo(request):
    return render(request, 'dashboard/faculty/faculty_CO.html')

def fQb(request):
    return render(request, 'dashboard/faculty/faculty_QB.html')

def sDashboard(request):
    return render(request, 'dashboard/student/student_dashboard.html')

def sCo(request):
    return render(request, 'dashboard/student/student_CO.html')

def sQb(request):
    return render(request, 'dashboard/student/student_QB.html')

def createQb(request):
    return render(request, 'dashboard/faculty/questionbank/createQB.html')

def createCo(request):
    return render(request, 'dashboard/faculty/courseoutline/createCO.html')

def viewAssessment(request):
    return render(request, 'dashboard/faculty/questionbank/viewAssessment.html')

