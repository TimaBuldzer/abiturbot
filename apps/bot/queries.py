from asgiref.sync import sync_to_async
from apps.users import models as user_models
from apps.main import models as main_models
import random


class User:

    @staticmethod
    @sync_to_async
    def get_user(tg_id):
        return user_models.User.objects.get(telegram_id=tg_id)

    @classmethod
    async def get_or_create_user(cls, tg_id, phone, name):

        try:
            await cls.get_user(tg_id)
        except user_models.User.DoesNotExist:
            await cls.create_user(phone, name, tg_id)

    @staticmethod
    @sync_to_async
    def create_user(phone, name, tg_id):
        user_models.User.objects.create(
            phone=phone,
            name=name,
            telegram_id=tg_id
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

    @classmethod
    @sync_to_async
    def get_test(cls, exclude):
        question = cls._get_question(exclude)
        answers = cls._get_answers(question)

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
