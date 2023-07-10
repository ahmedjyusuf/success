from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # StudentProfile fields
    pass

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TeacherProfile fields
    pass