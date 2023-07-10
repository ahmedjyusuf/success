from django.contrib import admin
from .models import ZoomClass, ZoomClassSchedule, DayOfWeek
# Register your models here.
admin.site.register(ZoomClass)
admin.site.register(ZoomClassSchedule)
admin.site.register(DayOfWeek)

