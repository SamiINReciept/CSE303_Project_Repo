from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(School_T)
admin.site.register(Department_T)
#admin.site.register(Employee_T)
admin.site.register(Dean_T)
admin.site.register(Head_T)
admin.site.register(Faculty_T)




