from django.contrib import admin
from .models import Question, Answer, Subject, Course, Lesson, UserAnswer

# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(UserAnswer)