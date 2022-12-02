from django.contrib import admin

# Register your models here.

from .models import *

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


class STUDENT_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in STUDENT_T._meta.fields if field.name != "id"]

admin.site.register(STUDENT_T, STUDENT_TAdmin)


class DEAN_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DEAN_T._meta.fields if field.name != "id"]

admin.site.register(DEAN_T, DEAN_TAdmin)


class DEPARTMENT_HEAD_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DEPARTMENT_HEAD_T._meta.fields if field.name != "id"]

admin.site.register(DEPARTMENT_HEAD_T, DEPARTMENT_HEAD_TAdmin)


class SCHOOL_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SCHOOL_T._meta.fields if field.name != "id"]

admin.site.register(SCHOOL_T, SCHOOL_TAdmin)


class DEPARTMENT_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DEPARTMENT_T._meta.fields if field.name != "id"]

admin.site.register(DEPARTMENT_T, DEPARTMENT_TAdmin)


class PROGRAM_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PROGRAM_T._meta.fields if field.name != "id"]

admin.site.register(PROGRAM_T, PROGRAM_TAdmin)


class FACULTY_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FACULTY_T._meta.fields if field.name != "id"]

admin.site.register(FACULTY_T, FACULTY_TAdmin)


class COURSE_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in COURSE_T._meta.fields if field.name != "id"]

admin.site.register(COURSE_T, COURSE_TAdmin)


class COCOURSE_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in COCOURSE_T._meta.fields if field.name != "id"]

admin.site.register(COCOURSE_T, COCOURSE_TAdmin)


class PLO_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PLO_T._meta.fields if field.name != "id"]

admin.site.register(PLO_T, PLO_TAdmin)


class CLO_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CLO_T._meta.fields if field.name != "id"]

admin.site.register(CLO_T, CLO_TAdmin)


class SECTION_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SECTION_T._meta.fields if field.name != "id"]

admin.site.register(SECTION_T, SECTION_TAdmin)


class ASSESSMENT_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ASSESSMENT_T._meta.fields if field.name != "id"]

admin.site.register(ASSESSMENT_T, ASSESSMENT_TAdmin)


class QUESTION_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in QUESTION_T._meta.fields if field.name != "id"]

admin.site.register(QUESTION_T, QUESTION_TAdmin)


class EVALUATION_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EVALUATION_T._meta.fields if field.name != "id"]

admin.site.register(EVALUATION_T, EVALUATION_TAdmin)


class COURSE_PREREQUISITE_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in COURSE_PREREQUISITE_T._meta.fields if field.name != "id"]

admin.site.register(COURSE_PREREQUISITE_T, COURSE_PREREQUISITE_TAdmin)


class COURSE_OUTLINE_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in COURSE_OUTLINE_T._meta.fields if field.name != "id"]

admin.site.register(COURSE_OUTLINE_T, COURSE_OUTLINE_TAdmin)


class COURSE_LESSON_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in COURSE_LESSON_T._meta.fields if field.name != "id"]

admin.site.register(COURSE_LESSON_T, COURSE_LESSON_TAdmin)


class COURSE_EVALUATION_TAdmin(admin.ModelAdmin):
    list_display = [field.name for field in COURSE_EVALUATION_T._meta.fields if field.name != "id"]

admin.site.register(COURSE_EVALUATION_T, COURSE_EVALUATION_TAdmin)