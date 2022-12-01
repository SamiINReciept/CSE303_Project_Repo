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
    EmployeeID = models.CharField(max_length=5, primary_key=True)
    EmployeeName = models.CharField(max_length=50, null=True)
    Email = models.CharField(max_length=30, null=True)
    EmployeeType = models.CharField(max_length=2, null=True)

    class Meta:
            abstract = True
            


class DEAN_T(EMPLOYEE_T):
    DEmployeeID = models.CharField(max_length=5)
    
    
    
class DEPARTMENT_HEAD_T(EMPLOYEE_T):
    DHEmployeeID = models.CharField(max_length=5)
 
    

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
    ProgramName = models.CharField(max_length=50)
    
    def __str__(self):
        return self.ProgramName



class FACULTY_T(EMPLOYEE_T):
    FEmployeeID = models.CharField(max_length=7)
    DepartmentID = models.ForeignKey(DEPARTMENT_T, on_delete=models.CASCADE)

    def __str__(self):
       return self.EmployeeName 
   
   

class COURSE_T(models.Model):
    CourseID = models.CharField(max_length=10, primary_key=True)
    CourseName = models.CharField(max_length=50, null=True)
    ProgramID = models.ForeignKey(PROGRAM_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.CourseID
    
    
    
class COCOURSE_T(models.Model):    
    CoCourseID = models.ForeignKey(COURSE_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.CoCourseID
    
    

class PLO_T(models.Model):
    PlOID = models.AutoField(primary_key=True)
    ProgramID = models.ForeignKey(PROGRAM_T, on_delete=models.CASCADE)
    PLONum = models.CharField(max_length=50)
    Details = models.CharField(max_length=200)
    
   
    def __str__(self):
        return self.PLONum



class CLO_T(models.Model):
    ClOID = models.AutoField(primary_key=True)
    PLOID = models.ForeignKey(PLO_T, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(COURSE_T, on_delete=models.CASCADE)
    CLONum = models.CharField(max_length=50)
    CLODescription = models.CharField(max_length=50)
    BloomC = models.CharField(max_length=50)
    BloomP = models.CharField(max_length=50)
    BloomA = models.CharField(max_length=50)
    COPOCorrelation = models.CharField(max_length=50)
   
    def __str__(self):
        return self.CLONum
    
    

class SECTION_T(models.Model):
    SectionID = models.CharField(primary_key=True)
    FEmployeeID = models.ForeignKey(FACULTY_T, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(COURSE_T, on_delete=models.CASCADE)
    SectionNum = models.IntegerField(max_length=10)
    Semester = models.IntegerField(max_length=10)
    Year = models.IntegerField(max_length=10)

    def __str__(self):
        return self.SectionID




class ASSESSMENT_T(models.Model):
    AssessmentID = models.CharField(primary_key=True)
    SectionID = models.ForeignKey(SECTION_T, on_delete=models.CASCADE)
    AssessmentName = models.CharField(max_length=50)
    TotalMarks = models.IntegerField(max_length=10)

    def __str__(self):
        return self.AssessmentName



class QUESTION_T(models.Model):
    QuestionID = models.CharField(primary_key=True)
    AssessmentID = models.ForeignKey(ASSESSMENT_T, on_delete=models.CASCADE)
    CLOID = models.ForeignKey(CLO_T, on_delete=models.CASCADE)
    QuestionNum = models.CharField(max_length=200)
    Details = models.CharField(max_length=200)
    Marks = models.IntegerField(max_length=200)
    
   
    def __str__(self):
        return self.QuestionID




class EVALUATION(models.Model):
    StudentID = models.ForeignKey(STUDENT_T, on_delete=models.CASCADE)
    StudentID = models.CharField(primary_key=True)
    
    StudentID = models.CharField(primary_key=True)
    QuestionID = models.ForeignKey(QUESTION_T, on_delete=models.CASCADE)
    
    ObtainedMarks = models.CharField(max_length=50)

   
    def __str__(self):
        return self.Evaluation


class COURSE_T(models.Model):
    CourseID = models.CharField(max_length=10, primary_key=True)
    CourseName = models.CharField(max_length=50, null=True)
    ProgramID = models.ForeignKey(PROGRAM_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.CourseID
    