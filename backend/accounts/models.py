from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from pytz import all_timezones

# Create your models here.


# class CustomUser(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)
#     timezone = models.CharField(max_length=100, choices=[(tz, tz) for tz in all_timezones])

# class Address(models.Model):
#     street = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     # Additional fields for address

#     def __str__(self):
#         return f"{self.street}, {self.city}, {self.state}"
    
# class Contact(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()
#     # Additional fields for contact

#     def __str__(self):
#         return f" Contact"
    
# class Teacher(models.Model):
#     name = models.CharField(max_length=100, null=False)
#     email = models.EmailField(max_length=100, null=True, blank=True)
#     password = models.CharField(max_length=255, null=False)
#     # department = models.ForeignKey(
#     #     'Department', on_delete=models.CASCADE, null=False, related_name='faculty')
#     # role = models.CharField(
#     #     default="Faculty", max_length=100, null=False, blank=True)
#     # photo = models.ImageField(upload_to='profile_pics', blank=True,
#     #                           null=False, default='profile_pics/default_faculty.png')

#     def delete(self, *args, **kwargs):
#         if self.photo != 'profile_pics/default_faculty.png':
#             self.photo.delete()
#         super().delete(*args, **kwargs)

#     class Meta:
#         verbose_name_plural = 'Faculty'

#     def __str__(self):
#         return self.name

# class Student(models.Model):
#     name = models.CharField(max_length=100, null=False)
#     email = models.EmailField(max_length=100, null=True, blank=True)
#     password = models.CharField(max_length=255, null=False)
#     # role = models.CharField(
#     #     default="Student", max_length=100, null=False, blank=True)
#     # course = models.ManyToManyField('Course', related_name='students', blank=True)
#     photo = models.ImageField(upload_to='profile_pics', blank=True,
#                               null=False, default='profile_pics/default_student.png')
#     subjects = models.ManyToManyField('lms.subject')

#     def delete(self, *args, **kwargs):
#         if self.photo != 'profile_pics/default_student.png':
#             self.photo.delete()
#         super().delete(*args, **kwargs)

#     class Meta:
#         verbose_name_plural = 'Students'

#     def __str__(self):
#         return self.name

# class Teacher(AbstractUser):
#     pass

# class Student(AbstractUser):
#     pass


