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
        
        deptname = request.POST['dept']
        schoolname = request.POST['school']
        coursecode = request.POST['COID']
        coursetitle = request.POST['Ctitle']
        coursetype = request.POST['Ctype']
        courseprereq = request.POST['Cprerequisite']
        creditvalue = request.POST['creditvalue']
        contacthour_week = request.POST['contact']
        coursedescription = request.POST['Cdescription']
        courseobjective = request.POST['CObjective']
        coursecontent = request.POST['CContent']
        assessmenttype = request.POST['Ctitle']
        referencebook = request.POST['reference']

        new_CourseOut = Course(deptname = deptname, schoolname = schoolname, coursecode = coursecode, coursetitle = coursetitle, coursetype = coursetype, courseprereq = courseprereq, 
        creditvalue = creditvalue, contacthour_week = contacthour_week, coursedescription = coursedescription, courseobjective = courseobjective, coursecontent = coursecontent,
        assessmenttype = assessmenttype, referencebook = referencebook)

        new_CourseOut.save()

        return render(request, 'dashboard/faculty/courseoutline/createCO.html')

    return render(request, 'dashboard/faculty/courseoutline/createCO.html', {"Department":display_dept, "School":display_school, "Course":display_course, "PLO":display_PLO})


def viewAssessment(request):
    
    return render(request, 'dashboard/faculty/questionbank/viewAssessment.html')

# Create your views here.
