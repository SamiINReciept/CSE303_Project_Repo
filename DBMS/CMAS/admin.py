from django.contrib import admin
from .models import*


# Register your models here.

#admin.site.register(STUDENT_T)
#admin.site.register(DEAN_T)
#admin.site.register(DEPARTMENT_HEAD_T)
#admin.site.register(SCHOOL_T)
#admin.site.register(DEPARTMENT_T)
#admin.site.register(PROGRAM_T)
#admin.site.register(FACULTY_T)
#admin.site.register(COURSE_T)
#admin.site.register(COCOURSE_T)
#admin.site.register(PLO_T)
#admin.site.register(CLO_T)
#admin.site.register(SECTION_T)
#admin.site.register(ASSESSMENT_T)
#admin.site.register(QUESTION_T)
#admin.site.register(EVALUATION_T)
#admin.site.register(COURSE_PREREQUISITE_T)
#admin.site.register(COURSE_OUTLINE_T)
#admin.site.register(COURSE_LESSON_T)
#admin.site.register(COURSE_EVALUATION_T)


class stdAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields if field.name != "id"]

admin.site.register(Student, stdAdmin)


class DAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dean._meta.fields if field.name != "id"]

admin.site.register(Dean, DAdmin)


class DHAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DepartmentHead._meta.fields if field.name != "id"]

admin.site.register(DepartmentHead, DHAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = [field.name for field in School._meta.fields if field.name != "id"]

admin.site.register(School, SchoolAdmin)


class DeptAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields if field.name != "id"]

admin.site.register(Department, DeptAdmin)


class ProgramAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Program._meta.fields if field.name != "id"]

admin.site.register(Program, ProgramAdmin)


class FAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Faculty._meta.fields if field.name != "id"]

admin.site.register(Faculty, FAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.fields if field.name != "id"]

admin.site.register(Course, CourseAdmin)


class PloAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Plo._meta.fields if field.name != "id"]

admin.site.register(Plo, PloAdmin)


class CloAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Clo._meta.fields if field.name != "id"]

admin.site.register(Clo, CloAdmin)


class SecAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Section._meta.fields if field.name != "id"]

admin.site.register(Section, SecAdmin)


class AssAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Assessment._meta.fields if field.name != "id"]

admin.site.register(Assessment, AssAdmin)


class QueAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields if field.name != "id"]

admin.site.register(Question, QueAdmin)


class EvalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Evaluation._meta.fields if field.name != "id"]

admin.site.register(Evaluation, EvalAdmin)


class COutAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CourseOutline._meta.fields if field.name != "id"]

admin.site.register(CourseOutline, COutAdmin)


class ClessonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CourseLesson._meta.fields if field.name != "id"]

admin.site.register(CourseLesson, ClessonAdmin)


class CevalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CourseEvaluation._meta.fields if field.name != "id"]

admin.site.register(CourseEvaluation, CevalAdmin)