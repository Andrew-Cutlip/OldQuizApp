from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Quiz, Question, Choice

# Create your views here.
def index(request):
    latest_quiz_list = Quiz.objects.order_by('-pub_date')[:5]
    template = loader.get_template('quiz/index.html')
    context = {
        'latest_quiz_list' : latest_quiz_list,
    }
    return HttpResponse(template.render(context, request))

def quiz(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist")
    return render(request, "quiz/quiz.html",
    {"quiz" : quiz})

def question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render( request, "quiz/question.html",
    {"question" : question})

def answer(request, quiz_id):
    quiz = get_object_or_404(Choice, pk=quiz_id)
    return render(request, 'quiz/choose.html',
    {'choice' : choice})
