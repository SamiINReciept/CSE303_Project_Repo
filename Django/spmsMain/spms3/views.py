from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
from spms3.models import *

# Create your views here.

display_dept = DEPARTMENT_T.objects.all()
display_school = SCHOOL_T.objects.all()
display_course = COURSE_T.objects.all()
display_PLO = PLO_T.objects.all()


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
    if request.method == 'POST':
        CourseDept = request.POST['dept']
        CourseSchool = request.POST['school']
        CourseCode = request.POST['COID']
        CourseTitle = request.POST['Ctitle']
        CourseType = request.POST['Ctype']
        CoursePrereq = request.POST['Cprerequisite']
        CreditValue = request.POST['creditvalue']
        ContactHourOrWeek = request.POST['contact']
        CourseDescription = request.POST['Cdescription']
        CourseObjective = request.POST['CObjective']
        CourseContent = request.POST['CContent']
        AssessmentType = request.POST['Ctitle']
        ReferenceBook = request.POST['reference']

        new_CourseOut = COURSE_OUTLINE_T(CourseDept=CourseDept, CourseSchool=CourseSchool, CourseCode=CourseCode, CourseTitle=CourseTitle, CourseType=CourseType, CoursePrereq=CoursePrereq, CreditValue=CreditValue,
                                         ContactHourOrWeek=ContactHourOrWeek, CourseDescription=CourseDescription, CourseObjective=CourseObjective, CourseContent=CourseContent, AssessmentType=AssessmentType,
                                         ReferenceBook=ReferenceBook)

        new_CourseOut.save()

    return render(request, 'dashboard/faculty/courseoutline/createCO.html', {"Dept_T": display_dept, "School_T": display_school, "Course_T": display_course, "PLO_T": display_PLO})


def viewAssessment(request):
    return render(request, 'dashboard/faculty/questionbank/viewAssessment.html')
