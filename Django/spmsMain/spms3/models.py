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
    DEmployeeID = models.ForeignKey(DEPARTMENT_HEAD_T, on_delete=models.CASCADE)
    SchoolName = models.CharField(max_length=50)

    def __str__(self):
        return self.SchoolID
   
   
    
class DEPARTMENT_T(models.Model):
    DepartmentID = models.CharField(max_length=5, primary_key=True)
    DepartmentName = models.CharField(max_length=50)
    SchoolID = models.ForeignKey(SCHOOL_T, on_delete=models.CASCADE)
    DHEmployeeID = models.ForeignKey(DEPARTMENT_HEAD_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.DepartmentID

class PROGRAM_T(models.Model):
    ProgramID = models.AutoField(primary_key=True)
    ProgramName = models.CharField(max_length=70)
    DepartmentID = models.ForeignKey(DEPARTMENT_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.programName


class FACULTY_T(EMPLOYEE_T):
    #facultyID = models.IntegerField(primary_key=True)
    joinDate = models.DateField(null=True)
    department = models.ForeignKey(DEPARTMENT_T, on_delete=models.CASCADE)

    def __str__(self):
       return self.firstName + " "+ self.lastName

class COURSE_T(models.Model):
    courseID = models.CharField(max_length=7, primary_key=True)
    courseName = models.CharField(max_length=50, null=True)
    numOfCredits = models.DecimalField(max_digits=2, decimal_places=1)
    program = models.ForeignKey(PROGRAM_T, on_delete=models.CASCADE)
    courseType = models.CharField(max_length=15)

    def __str__(self):
        return self.courseID

class PLO_T(models.Model):
    ploID = models.AutoField(primary_key=True)
    ploNum = models.CharField(max_length=5)
    details = models.CharField(max_length=50)
    program = models.ForeignKey(PROGRAM_T, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.ploNum



