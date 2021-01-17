from asgiref.sync import sync_to_async

from apps.main import models as main_models


async def calculate_score(dictionary):
    data = {
        'ids': [i.get('id') for i in list(dictionary.values())],
        'vars': [i.get('var') for i in list(dictionary.values())]
    }
    l = len(list(dictionary.values()))
    right = sum([1
                 for i, v in enumerate(data.get('ids')) if data.get('vars')[i] == await get_question_answer(v)
                 ])
    print(right)
    return right, l - right, l


@sync_to_async
def get_question_answer(v):
    return main_models.Question.objects.get(id=v).answer_set.get(is_right=True).letter
