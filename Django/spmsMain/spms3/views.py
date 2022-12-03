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


def viewCo(request):
    course_outline = COURSE_OUTLINE_T.objects.all()
    # clo_table = CLO_T.objects.all()
    # course_lesson = COURSE_LESSON_T.objects.all()
    # course_evaluation = COURSE_EVALUATION_T.objects.all()
    # , {'clo_table': clo_table}, {'course_lesson': course_lesson}, {'course_eval': course_evaluation}

    return render(request, 'dashboard/faculty/courseoutline/ViewCO.html', {'course_outline': course_outline})


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

        CourseID = COURSE_T.objects.get(CourseID=CourseCode)

        CLONum = request.POST['clo1']
        CLODescription = request.POST['clo1desc']
        BloomC = request.POST['clo1C']
        BloomP = request.POST['clo1P']
        BloomA = request.POST['clo1A']
        COPOCorrelation = request.POST['CP1']
        new_Clo = CLO_T(CLONum=CLONum, CourseID=CourseID, CLODescription=CLODescription,
                        BloomC=BloomC, BloomP=BloomP, BloomA=BloomA, COPOCorrelation=COPOCorrelation)
        new_Clo.save()

        CLONum = request.POST['clo2']
        CLODescription = request.POST['clo2desc']
        BloomC = request.POST['clo2C']
        BloomP = request.POST['clo2P']
        BloomA = request.POST['clo2A']
        COPOCorrelation = request.POST['CP2']
        new_Clo = CLO_T(CLONum=CLONum, CourseID=CourseID, CLODescription=CLODescription,
                        BloomC=BloomC, BloomP=BloomP, BloomA=BloomA, COPOCorrelation=COPOCorrelation)
        new_Clo.save()

        CLONum = request.POST['clo3']
        CLODescription = request.POST['clo3desc']
        BloomC = request.POST['clo3C']
        BloomP = request.POST['clo3P']
        BloomA = request.POST['clo3A']
        COPOCorrelation = request.POST['CP3']
        new_Clo = CLO_T(CLONum=CLONum, CourseID=CourseID, CLODescription=CLODescription,
                        BloomC=BloomC, BloomP=BloomP, BloomA=BloomA, COPOCorrelation=COPOCorrelation)
        new_Clo.save()

        CLONum = request.POST['clo4']
        CLODescription = request.POST['clo4desc']
        BloomC = request.POST['clo4C']
        BloomP = request.POST['clo4P']
        BloomA = request.POST['clo4A']
        COPOCorrelation = request.POST['CP4']
        new_Clo = CLO_T(CLONum=CLONum, CourseID=CourseID, CLODescription=CLODescription,
                        BloomC=BloomC, BloomP=BloomP, BloomA=BloomA, COPOCorrelation=COPOCorrelation)
        new_Clo.save()

        CLONum = request.POST['clo5']
        CLODescription = request.POST['clo5desc']
        BloomC = request.POST['clo5C']
        BloomP = request.POST['clo5P']
        BloomA = request.POST['clo5A']
        COPOCorrelation = request.POST['CP5']
        new_Clo = CLO_T(CLONum=CLONum, CourseID=CourseID, CLODescription=CLODescription,
                        BloomC=BloomC, BloomP=BloomP, BloomA=BloomA, COPOCorrelation=COPOCorrelation)
        new_Clo.save()

    return render(request, 'dashboard/faculty/courseoutline/createCO.html', {"Dept_T": display_dept, "School_T": display_school, "Course_T": display_course, "PLO_T": display_PLO})


def viewAssessment(request):
    return render(request, 'dashboard/faculty/questionbank/viewAssessment.html')
