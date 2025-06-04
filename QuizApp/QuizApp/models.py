from django.db import models

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=300)
    points = models.IntegerField(default=0)

    def __str__(self):
        answers = self.question.answers.order_by('id')
        index = list(answers).index(self) + 1
        return f"Question {self.question.id} - Answer {index}"
