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

    quiz_obj = Quiz.objects.first()
    max_points = 0
    for question in quiz_obj.questions.all():
        max_points += max(answer.points for answer in question.answers.all())

    percentage = (total_points / max_points * 100) if max_points > 0 else 0

    if percentage >= 75:
        message = "You have very healthy habits!"
    elif percentage >= 50:
        message = "There's some room for improvement in your habits."
    else:
        message = "Consider making some changes to improve your daily habits."

    context = {
        'app_name': 'Quiz App',
        'total_points': total_points,
        'max_points': max_points,
        'percentage': round(percentage, 1),
        'message': message
    }

    return render(request, 'result.html', context)
