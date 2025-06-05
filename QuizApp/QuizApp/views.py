from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html', {'app_name': 'Quiz App'})

def quiz(request):
    quiz_obj = Quiz.objects.first()
    questions = quiz_obj.questions.all()

    if request.method == 'POST':
        total_points = 0
        for question in questions:
            answer_id = request.POST.get(f'question_{question.id}')
            if answer_id:
                answer = Answer.objects.get(id=answer_id)
                total_points += answer.points

        request.session['quiz_points'] = total_points
        return redirect('result')

    return render(request, 'quiz.html', {'app_name': 'Quiz App', 'quiz': quiz_obj, 'questions': questions})

def result(request):
    total_points = request.session.get('quiz_points', 0)
    return render(request, 'result.html', {'app_name': 'Quiz App', 'total_points': total_points})
