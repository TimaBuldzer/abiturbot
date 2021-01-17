from django.urls import path
from . import views as rest_views
from apps.bot import bot

urlpatterns = [
    path('questions/', rest_views.QuestionView.as_view()),
    path('', bot.telegram_bot_start),
]
