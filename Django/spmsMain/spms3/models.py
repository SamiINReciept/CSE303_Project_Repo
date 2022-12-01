from django.db import models

# Create your models here.



class STUDENT_T(models.Model):
    StudentID = models.CharField(max_length=7, primary_key=True)
    StudentName = models.CharField(max_length=50, null=True)
    Email = models.CharField(max_length=50, null=True)
    ProgramID = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.StudentID



class EMPLOYEE_T(models.Model):
    EmployeeID = models.CharField(max_length=4, primary_key=True)
    EmployeeName = models.CharField(max_length=30, null=True)
    Email = models.CharField(max_length=30, null=True)
    EmployeeType = models.CharField(max_length=1, null=True)

    class Meta:
            abstract = True
            


class DEAN_T(EMPLOYEE_T):
    DEmployeeID = models.CharField(max_length=5, primary_key=True)
    
    
    
class DEPARTMENT_HEAD_T(EMPLOYEE_T):
    DHEmployeeID = models.CharField(max_length=4, primary_key=True)
 
    

class SCHOOL_T(models.Model):
    SchoolID = models.CharField(max_length=5, primary_key=True)
    DEmployeeID = models.ForeignKey(DEAN_T, on_delete=models.CASCADE)
    SchoolName = models.CharField(max_length=50)

    def __str__(self):
        return self.SchoolID
   
   
    
class DEPARTMENT_T(models.Model):
    DepartmentID = models.CharField(max_length=5, primary_key=True)
    SchoolID = models.ForeignKey(SCHOOL_T, on_delete=models.CASCADE)
    DHEmployeeID = models.ForeignKey(DEPARTMENT_HEAD_T, on_delete=models.CASCADE)
    DepartmentName = models.CharField(max_length=50)

    def __str__(self):
        return self.DepartmentID
    
    

class PROGRAM_T(models.Model):
    ProgramID = models.AutoField(primary_key=True)
    DepartmentID = models.ForeignKey(DEPARTMENT_T, on_delete=models.CASCADE)
    ProgramName = models.CharField(max_length=70)
    
    def __str__(self):
        return self.ProgramName



class FACULTY_T(EMPLOYEE_T):
    FEmployeeID = models.CharField(max_length=7, primary_key=True)
    DepartmentID = models.ForeignKey(DEPARTMENT_T, on_delete=models.CASCADE)

    def __str__(self):
       return self.firstName + " "+ self.lastName
   
   

class COURSE_T(models.Model):
    CourseID = models.CharField(max_length=7, primary_key=True)
    CourseName = models.CharField(max_length=50, null=True)
    numOfCredits = models.DecimalField(max_digits=2, decimal_places=1)
    ProgramID = models.ForeignKey(PROGRAM_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.courseID
    
    
class COCOURSE_T(models.Model):    
    CoCourseID = models.ForeignKey(COURSE_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.courseID
    
    

class PLO_T(models.Model):
    ploID = models.AutoField(primary_key=True)
    ploNum = models.CharField(max_length=5)
    details = models.CharField(max_length=50)
    program = models.ForeignKey(PROGRAM_T, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.ploNum



