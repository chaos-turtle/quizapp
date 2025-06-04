from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html', context={'app_name': 'Quiz App'})

def quiz(request):
    quiz_obj = Quiz.objects.first()
    return render(request, 'quiz.html', context={'app_name': 'Quiz App', 'quiz': quiz_obj})