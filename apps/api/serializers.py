from rest_framework import serializers
from apps.main import models as main_models


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = main_models.Question
        fields = '__all__'
