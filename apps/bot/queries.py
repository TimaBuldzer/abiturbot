from apps.main import models as main_models
import random


class SubjectTest:

    @staticmethod
    def _get_question(exclude):
        questions = main_models.Question.objects.exclude(id__in=exclude)
        return random.choice(questions)

    @staticmethod
    def _get_answers(question):
        answers = main_models.Answer.objects.filter(question=question)
        return answers

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
