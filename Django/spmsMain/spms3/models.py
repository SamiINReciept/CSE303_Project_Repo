from django.db import models

# Create your models here.

class School_T(models.Model):
    schoolID = models.CharField(max_length=5, primary_key=True)
    schoolName = models.CharField(max_length=50)

    def __str__(self):
        return self.schoolID


class Department_T(models.Model):
    departmentID = models.CharField(max_length=5, primary_key=True)
    departmentName = models.CharField(max_length=50)
    school = models.ForeignKey(School_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.departmentID


class Program_T(models.Model):
    programID = models.AutoField(primary_key=True)
    programName = models.CharField(max_length=70)
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE, default='N/A')

    def __str__(self):
        return self.programName

class Student_T(models.Model):
    studentID = models.CharField(max_length=7, primary_key=True)
    Name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    enrollmentDate = models.DateField(null=True)
    #program = models.ForeignKey(Program_T, on_delete=models.CASCADE, default='N/A')
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.studentID


class Employee_T(models.Model):
    employeeID = models.CharField(max_length=4, primary_key=True)
    employeeName = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    employeeType = models.CharField(max_length=1, null=True)

    class Meta:
            abstract = True

class Dean_T(Employee_T):
    #deanID = models.CharField(max_length=4, primary_key=True)
    startDate = models.CharField(max_length=15, default='N/A')
    endDate = models.CharField(max_length=15, default='N/A')
    school = models.ForeignKey(School_T, on_delete=models.CASCADE)

class Head_T(Employee_T):
    #headID = models.CharField(max_length=4, primary_key=True)
    startDate = models.CharField(max_length=15,default='N/A')
    endDate = models.CharField(max_length=15,default='N/A')
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE)


class Faculty_T(Employee_T):
    #facultyID = models.IntegerField(primary_key=True)
    joinDate = models.DateField(null=True)
    department = models.ForeignKey(Department_T, on_delete=models.CASCADE)

    def __str__(self):
       return self.firstName + " "+ self.lastName

class Course_T(models.Model):
    courseID = models.CharField(max_length=7, primary_key=True)
    courseName = models.CharField(max_length=50, null=True)
    numOfCredits = models.DecimalField(max_digits=2, decimal_places=1)
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE)
    courseType = models.CharField(max_length=15)

    def __str__(self):
        return self.courseID

class PLO_T(models.Model):
    ploID = models.AutoField(primary_key=True)
    ploNum = models.CharField(max_length=5)
    details = models.CharField(max_length=50)
    program = models.ForeignKey(Program_T, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.ploNum



