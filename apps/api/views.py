from rest_framework import generics
from rest_framework import permissions
from . import serializers as rest_serializers
from apps.main import models as main_models


class QuestionView(generics.ListAPIView):
    serializer_class = rest_serializers.QuestionSerializer
    permission_classes = [permissions.AllowAny]
    queryset = main_models.Question.objects.all()
