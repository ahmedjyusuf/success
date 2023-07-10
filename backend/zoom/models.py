from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
import pytz
import os
import django


User = get_user_model
class ZoomClass(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.URLField()
    name = models.CharField(max_length=255, null=True, blank=True)
    repeat = models.BooleanField(default=True)
    # ZoomClass fields
    def __str__(self):
        return self.name

class DayOfWeek(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class ZoomClassSchedule(models.Model):
    zoom_class = models.ForeignKey(ZoomClass, on_delete=models.CASCADE)
    student = models.ManyToManyField(settings.AUTH_USER_MODEL)
    class_time = models.DateTimeField()
    days_of_week = models.ManyToManyField(DayOfWeek)
    repeat = models.BooleanField(default=True)

    def __str__(self):
        string = f'{str(self.zoom_class.name)} - {str(self.class_time.tzname())}' if self.zoom_class.name else str(self.class_time.time())
        return string
