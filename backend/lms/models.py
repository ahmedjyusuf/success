from django.db import models
from django.conf import settings
# Create your models here.



from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Subject(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self) -> str:
        return self.name
    
class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.Case)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self) -> str:
        return self.name



class Lesson(models.Model):
    number = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def total_questions(self):
        #Question.objects.filter(lesson=self).count()
        return self.question_set.count()
    
    def __str__(self) -> str:
        # print('\n\nqs')
        return f" Lesson: {str(self.number)}" 



class Question(models.Model):
    text = models.CharField(max_length=200)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.text
    
    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text
    

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def correct_answer(self):
        return self.selected_answer.correct
    def __str__(self) -> str:
        return f"{self.user.username} - {self.question.text}"
    
class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     # Enrollment fields
#     pass
class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#     # Assignment fields
#     pass

# class Submission(models.Model):
#     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
#     student = models.ForeignKey(User, on_delete=models.CASCADE)
#     # Submission fields
#     pass

# class Grade(models.Model):
#     submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
#     # Grade fields
#     pass


# class Subject(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
