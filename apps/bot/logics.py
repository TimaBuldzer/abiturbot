from apps.main import models as main_models


async def calculate_score(dictionary):
    data = {
        'ids': [i.get('id') for i in list(dictionary.values())],
        'vars': [i.get('var') for i in list(dictionary.values())]
    }
    right = sum([1
                 for i, v in enumerate(data.get('ids')) if data.get('vars')[i] == get_question_answer(v)
                 ])

    return right, 30 - right, 30


async def get_question_answer(v):
    return main_models.Question.objects.get(id=v).answer_set.get(is_right=True).letter
