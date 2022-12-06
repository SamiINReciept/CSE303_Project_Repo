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
    if request.method == 'POST':
        
        Deptname = request.POST['dept']
        Schoolname = request.POST['school']
        Coursecode = request.POST['COID']
        Coursetitle = request.POST['Ctitle']
        Coursetype = request.POST['Ctype']
        Courseprereq = request.POST['Cprerequisite']
        Creditvalue = request.POST['creditvalue']
        Contacthour_week = request.POST['contact']
        Coursedescription = request.POST['Cdescription']
        Courseobjective = request.POST['CObjective']
        Coursecontent = request.POST['CContent']
        Assessmenttype = request.POST['Ctitle']
        Referencebook = request.POST['reference']

        new_CourseOut = Course(deptname = Deptname, schoolname = Schoolname, coursecode = Coursecode, coursetitle = Coursetitle, coursetype = Coursetype, courseprereq = Courseprereq, 
        creditvalue = Creditvalue, contacthour_week = Contacthour_week, coursedescription = Coursedescription, courseobjective = Courseobjective, coursecontent = Coursecontent,
        assessmenttype = Assessmenttype, referencebook = Referencebook)

        new_CourseOut.save()

        # return render(request, 'dashboard/faculty/courseoutline/createCO.html')

    return render(request, 'dashboard/faculty/courseoutline/createCO.html', {"Department":display_dept, "School":display_school, "Course":display_course, "PLO":display_PLO})


def viewAssessment(request):
    
    return render(request, 'dashboard/faculty/questionbank/viewAssessment.html')

# Create your views here.
