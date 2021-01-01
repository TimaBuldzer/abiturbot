from django.urls import path
from .views import TestRuParser

urlpatterns = [
    path('', TestRuParser.as_view())
]
