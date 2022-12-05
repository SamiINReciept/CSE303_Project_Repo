from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class user(AbstractUser):
#     class role(models.TextChoices):
#         admin = "admin", 'admin'
#         faculty = "faculty", 'faculty'
#         student = "student", 'student'

#     base_role = role.admin

#     role = models.CharField(max_length='50', choices=role.choices)

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(*args, **kwargs)
