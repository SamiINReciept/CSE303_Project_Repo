from django.shortcuts import render
from CMAS.models import *

# Create your views here.

display_dept = Department.objects.all()
display_school = School.objects.all()
display_course = Course.objects.all()
display_PLO = Plo.objects.all()

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


def viewCo(request):
    return render(request, 'dashboard/faculty/courseoutline/ViewCO.html')


def createCo(request):
    # if request.method == 'POST':
        # CourseDept = request.POST['dept']
        # CourseSchool = request.POST['school']
        # CourseCode = request.POST['COID']
        # CourseTitle = request.POST['Ctitle']
        # CourseType = request.POST['Ctype']
        # CoursePrereq = request.POST['Cprerequisite']
        # CreditValue = request.POST['creditvalue']
        # ContactHourOrWeek = request.POST['contact']
        # CourseDescription = request.POST['Cdescription']
        # CourseObjective = request.POST['CObjective']
        # CourseContent = request.POST['CContent']
        # AssessmentType = request.POST['Ctitle']
        # ReferenceBook = request.POST['reference']

        # new_CourseOut = Course()

        # new_CourseOut.save()

        # return render(request, 'dashboard/faculty/courseoutline/createCO.html')

    return render(request, 'dashboard/faculty/courseoutline/createCO.html', {"Department":display_dept, "School":display_school, "Course":display_course, "PLO":display_PLO})


def viewAssessment(request):
    
    return render(request, 'dashboard/faculty/questionbank/viewAssessment.html')

# Create your views here.
