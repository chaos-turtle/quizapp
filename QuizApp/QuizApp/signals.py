from django.db.models.signals import pre_delete, post_delete, pre_save, post_save
from django.dispatch import receiver
from QuizApp.models import *