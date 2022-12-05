from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    admin = models.BooleanField('Admin', default=False)
    faculty = models.BooleanField('Faculty', default=False)
    student = models.BooleanField('Student', default=False)