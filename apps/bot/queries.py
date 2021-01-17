from asgiref.sync import sync_to_async
from apps.users import models as user_models
from apps.main import models as main_models
from apps.bot import messages
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

    def __init__(self, subject):
        self.subject = subject

    def _get_question(self, exclude):
        questions = main_models.Question.objects.exclude(id__in=exclude).filter(
            subject__name__icontains=self.subject).distinct()
        try:
            return random.choice(questions)
        except IndexError:
            return None

    @staticmethod
    def _get_answers(question):
        answers = main_models.Answer.objects.filter(question=question)
        return answers

    @sync_to_async
    def get_test(self, exclude):
        question = self._get_question(exclude)
        if not question:
            return None
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

    @staticmethod
    async def cast_to_string(test):
        return messages.question_message.format(
            test.get('question').get('text'),
            '\n'.join((answer.get('answer') for answer in test.get('answers')))
        )
