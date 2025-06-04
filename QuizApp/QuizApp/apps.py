from django.apps import AppConfig


class QuizappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QuizApp'

    def ready(self):
        from . import signals
