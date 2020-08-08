from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quiz_id>/', views.quiz, name="quiz"),
    path('<int:quiz_id>/choice/', views.Choice, name="choice")
]
