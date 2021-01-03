from asgiref.sync import sync_to_async
from apps.users import models as user_models
from apps.main import models as main_models
import random


class User:

    def __init__(self):
        self.phone = None
        self.tg_id = None
        self.name = None

    @sync_to_async
    def get_user(self):
        return user_models.User.objects.get(telegram_id=self.tg_id)

    async def check_if_user_exists(self, tg_id, phone, name):

        self.phone = phone
        self.tg_id = tg_id
        self.name = name

        try:
            await self.get_user()
        except user_models.User.DoesNotExist:
            await self.create_user()

    @sync_to_async
    def create_user(self):
        user_models.User.objects.create(
            phone=self.phone,
            name=self.name,
            telegram_id=self.tg_id
        )


class SubjectTest:

    @staticmethod
    def _get_question(exclude):
        questions = main_models.Question.objects.exclude(id__in=exclude)
        return random.choice(questions)

    @staticmethod
    def _get_answers(question):
        answers = main_models.Answer.objects.filter(question=question)
        return answers

    @sync_to_async
    def get_test(self, exclude):
        question = self._get_question(exclude)
        answers = self._get_answers(question)

        return {
            'question': {
                'id': question.id,
                'text': question.question
            },
            'answers': [{
                'id': answer.id,
                'answer': answer.letter + ') ' + answer.answer,
                'var': answer.letter
            }
                for answer in answers
            ]
        }
