from django.contrib import admin

# Register your models here.
from .models import Question, Quiz, User, Choice

admin.site.register(User)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)