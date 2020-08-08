from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField("username", max_length=50)

    def __str__(self):
        return self.username

class Quiz(models.Model):
    author = models.ForeignKey(User,
    on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.quiz_name

DEFAULT_QUIZ_ID = 1
class Question(models.Model):
    quiz = models.ForeignKey(Quiz,
    on_delete=models.CASCADE, default=DEFAULT_QUIZ_ID)
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

DEFAULT_BOOL = False
class Choice(models.Model):
    question = models.ForeignKey(Question,
    on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct_choice = models.BooleanField("correct", default=DEFAULT_BOOL)

    def __str__(self):
        return self.choice_text