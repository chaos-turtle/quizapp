from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html', {'app_name': 'Quiz App'})

def quiz(request):
    quiz_obj = Quiz.objects.first()
    questions = quiz_obj.questions.order_by('?')

    if request.method == 'POST':
        total_points = 0
        for question in quiz_obj.questions.all():
            answer_id = request.POST.get(f'question_{question.id}')
            if answer_id:
                answer = Answer.objects.get(id=answer_id)
                total_points += answer.points

        request.session['quiz_points'] = total_points
        return redirect('result')

    randomized_questions = []
    for question in questions:
        # Randomize answers for each question
        randomized_answers = question.answers.order_by('?')
        randomized_questions.append({
            'question': question,
            'answers': randomized_answers
        })

    return render(request, 'quiz.html', {'app_name': 'Quiz App', 'quiz': quiz_obj, 'questions': randomized_questions})

def result(request):
    total_points = request.session.get('quiz_points', 0)

    quiz_obj = Quiz.objects.first()
    max_points = 0
    for question in quiz_obj.questions.all():
        max_points += max(answer.points for answer in question.answers.all())

    percentage = (total_points / max_points * 100) if max_points > 0 else 0

    if percentage >= 75:
        message = "Good job! You have very healthy habits!"
    elif percentage >= 50:
        message = "Your habits are generally healthy, however, there's still some room for improvement."
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
