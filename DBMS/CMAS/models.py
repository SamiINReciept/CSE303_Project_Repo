# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class School(models.Model):
    schoolid = models.AutoField(db_column='SchoolID', primary_key=True)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    schooldetails = models.CharField(db_column='SchoolDetails', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'school'

    def __str__(self):
        return self.schoolname
        

class Department(models.Model):
    departmentid = models.AutoField(db_column='DepartmentID', primary_key=True)  # Field name made lowercase.
    schoolid = models.ForeignKey('School', models.DO_NOTHING, db_column='SchoolID', blank=True, null=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=65, blank=True, null=True)  # Field name made lowercase.
    departmentdetails = models.CharField(db_column='DepartmentDetails', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'

    def __str__(self):
        return self.departmentname


class Employee(models.Model):
    employeeid = models.IntegerField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    employeename = models.CharField(db_column='EmployeeName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'
        abstract = True


class Dean(Employee):
    demployeeid = models.OneToOneField('Employee', models.DO_NOTHING, db_column='DemployeeID', primary_key=True)  # Field name made lowercase.
    schoolid = models.ForeignKey('School', models.DO_NOTHING, db_column='SchoolID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dean'


class DepartmentHead(Employee):
    dhemployeeid = models.OneToOneField('Employee', models.DO_NOTHING, db_column='DHEmployeeID', primary_key=True)  # Field name made lowercase.
    departmentid = models.ForeignKey(Department, models.DO_NOTHING, db_column='DepartmentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department_head'


class Faculty(Employee):
    femployeeid = models.OneToOneField(Employee, models.DO_NOTHING, db_column='FEmployeeID', primary_key=True)  # Field name made lowercase.
    departmentid = models.ForeignKey(Department, models.DO_NOTHING, db_column='DepartmentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faculty'

    def __str__(self):
        return self.employeename

        
class Program(models.Model):
    programid = models.AutoField(db_column='ProgramID', primary_key=True)  # Field name made lowercase.
    departmentid = models.ForeignKey(Department, models.DO_NOTHING, db_column='DepartmentID', blank=True, null=True)  # Field name made lowercase.
    programname = models.CharField(db_column='ProgramName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    programdetail = models.CharField(db_column='ProgramDetail', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'program'

    def __str__(self):
        return self.programname

class Plo(models.Model):
    ploid = models.AutoField(db_column='PLOID', primary_key=True)  # Field name made lowercase.
    programid = models.ForeignKey('Program', models.DO_NOTHING, db_column='ProgramID', blank=True, null=True)  # Field name made lowercase.
    plonum = models.CharField(db_column='PLONum', max_length=45, blank=True, null=True)  # Field name made lowercase.
    plodetail = models.CharField(db_column='PLODetail', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plo'

    def __str__(self):
        return self.programid + " " + self.plonum


class Student(models.Model):
    studentid = models.CharField(db_column='StudentID', primary_key=True, max_length=50)  # Field name made lowercase.
    studentname = models.CharField(db_column='StudentName', max_length=75, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=75, blank=True, null=True)  # Field name made lowercase.
    programid = models.ForeignKey(Program, models.DO_NOTHING, db_column='ProgramID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self):
        return self.studentname


class Course(models.Model):
    courseid = models.AutoField(db_column='CourseID', primary_key=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='CourseName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    programid = models.ForeignKey('Program', models.DO_NOTHING, db_column='ProgramID', blank=True, null=True)  # Field name made lowercase.
    coursedescription = models.CharField(db_column='CourseDescription', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    coursedetail = models.CharField(db_column='CourseDetail', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'

    def __str__(self):
        return self.coursename


class Clo(models.Model):
    cloid = models.AutoField(db_column='CLOID', primary_key=True)  # Field name made lowercase.
    ploid = models.ForeignKey('Plo', models.DO_NOTHING, db_column='PLOID')  # Field name made lowercase.
    courseid = models.ForeignKey('Course', models.DO_NOTHING, db_column='CourseID')  # Field name made lowercase.
    clonum = models.CharField(db_column='CLONum', max_length=45)  # Field name made lowercase.
    clodescription = models.CharField(db_column='CLODescription', max_length=2000)  # Field name made lowercase.
    bloomc = models.CharField(db_column='BloomC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bloomp = models.CharField(db_column='BloomP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    blooma = models.CharField(db_column='BloomA', max_length=45, blank=True, null=True)  # Field name made lowercase.
    copocorrelation = models.CharField(db_column='COPOCorrelation', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clo'

    def __str__(self):
        return self.courseid + " " + self.clonum


class Section(models.Model):
    sectionid = models.AutoField(db_column='SectionID', primary_key=True)  # Field name made lowercase.
    femployeeid = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='FEmployeeID', blank=True, null=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseID', blank=True, null=True)  # Field name made lowercase.
    sectionnum = models.CharField(db_column='SectionNum', max_length=45, blank=True, null=True)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'section'

    def __str__(self):
        return self.courseid + " " + self.sectionnum


class Assessment(models.Model):
    assessmentid = models.AutoField(db_column='AssessmentID', primary_key=True)  # Field name made lowercase.
    sectionid = models.ForeignKey('Section', models.DO_NOTHING, db_column='SectionID', blank=True, null=True)  # Field name made lowercase.
    assessmentname = models.CharField(db_column='AssessmentName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    totalmarks = models.IntegerField(db_column='TotalMarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assessment'

    def __str__(self):
        return Section.sectionnum + " " + self.assessmentname


class Question(models.Model):
    questionid = models.AutoField(db_column='QuestionID', primary_key=True)  # Field name made lowercase.
    assessmentid = models.ForeignKey(Assessment, models.DO_NOTHING, db_column='AssessmentID', blank=True, null=True)  # Field name made lowercase.
    cloid = models.ForeignKey(Clo, models.DO_NOTHING, db_column='CLOID', blank=True, null=True)  # Field name made lowercase.
    questionnumber = models.CharField(db_column='QuestionNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    questiondetail = models.CharField(db_column='QuestionDetail', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    marks = models.IntegerField(db_column='Marks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'question'

    def __str__(self):
        return Assessment.assessmentname + " " + self.questionnumber

class Evaluation(models.Model):
    studentid = models.IntegerField(db_column='StudentID', primary_key=True)  # Field name made lowercase.
    questionid = models.ForeignKey('Question', models.DO_NOTHING, db_column='QuestionID')  # Field name made lowercase.
    obtainedmarks = models.IntegerField(db_column='ObtainedMarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evaluation'
        unique_together = (('studentid', 'questionid'),)

    def __str__(self):
        return self.studentid + " " + self.questionid


class CourseOutline(models.Model):
    courseid = models.OneToOneField(Course, models.DO_NOTHING, db_column='CourseID', primary_key=True)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=400, blank=True, null=True)  # Field name made lowercase.
    coursecode = models.CharField(db_column='CourseCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    coursetitle = models.CharField(db_column='CourseTitle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    coursetype = models.CharField(db_column='CourseType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    creditvalue = models.CharField(db_column='CreditValue', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contacthour_week = models.CharField(db_column='ContactHour/Week', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coursedescription = models.CharField(db_column='CourseDescription', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    courseobjective = models.CharField(db_column='CourseObjective', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    coursecontent = models.CharField(db_column='CourseContent', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    assessmenttype = models.CharField(db_column='AssessmentType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    referencebook = models.CharField(db_column='ReferenceBook', max_length=3000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course_outline'

    def __str__(self):
        return self.coursecode


class CourseLesson(models.Model):
    courseid = models.OneToOneField('CourseOutline', models.DO_NOTHING, db_column='CourseID', primary_key=True)  # Field name made lowercase.
    week = models.CharField(db_column='Week', max_length=45)  # Field name made lowercase.
    topic = models.CharField(db_column='Topic', max_length=45, blank=True, null=True)  # Field name made lowercase.
    teachingstrategy = models.CharField(db_column='TeachingStrategy', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    assessmentstrategy = models.CharField(db_column='AssessmentStrategy', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    clolevel = models.CharField(db_column='CLOLevel', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course_lesson'
        unique_together = (('courseid', 'week'),)

    def __str__(self):
        return self.courseid + " " + self.week


class CourseEvaluation(models.Model):
    courseid = models.OneToOneField(Course, models.DO_NOTHING, db_column='CourseID', primary_key=True)  # Field name made lowercase.
    assessmenttools = models.CharField(db_column='AssessmentTools', max_length=45)  # Field name made lowercase.
    marksdistribution = models.CharField(db_column='MarksDistribution', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bloomcategory = models.CharField(db_column='BloomCategory', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course_evaluation'
        unique_together = (('courseid', 'assessmenttools'),)

    def __str__(self):
        return self.courseid + " " + self.assessmenttools













