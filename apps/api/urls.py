from django.urls import path
from . import views as rest_views

urlpatterns = [
    path('questions/', rest_views.QuestionView.as_view()),
]
