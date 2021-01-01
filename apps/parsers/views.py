import json

from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework.response import Response
from apps.main import models


class CreateTest(GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.data)
        question = self.create_question(data)
        self.create_answers(data, question)
        return Response({'ok': 'success'})

    @staticmethod
    def create_question(data):
        question = models.Question.objects.create(
            question=data.get('task'),
            subject_id=data.get('subject'),
            source_id=data.get('source')
        )
        return question

    @staticmethod
    def create_answers(data, question):
        for answer in data.get('answers'):
            models.Answer.objects.create(
                question=question,
                answer=answer.get('answer'),
                letter=answer.get('variant'),
                is_right=True if answer.get('variant').lower() == data.get('right').lower() else False
            )
