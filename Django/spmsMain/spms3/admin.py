from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(STUDENT_T)
admin.site.register(DEAN_T)
admin.site.register(DEPARTMENT_HEAD_T)
admin.site.register(SCHOOL_T)
admin.site.register(DEPARTMENT_T)
admin.site.register(PROGRAM_T)
admin.site.register(FACULTY_T)
admin.site.register(COURSE_T)
admin.site.register(COCOURSE_T)
admin.site.register(PLO_T)
admin.site.register(CLO_T)
admin.site.register(SECTION_T)
admin.site.register(ASSESSMENT_T)
admin.site.register(QUESTION_T)
admin.site.register(EVALUATION_T)
admin.site.register(COURSE_PREREQUISITE_T)
admin.site.register(COURSE_OUTLINE_T)
admin.site.register(COURSE_LESSON_T)
admin.site.register(COURSE_EVALUATION_T)