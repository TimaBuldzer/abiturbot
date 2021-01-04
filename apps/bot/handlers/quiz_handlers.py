from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from apps.bot import states, logics, messages
from apps.bot.queries import SubjectTest
from apps.bot.misc import dp

tests = SubjectTest()


@dp.callback_query_handler(lambda c: c.data == 'start_test')
async def process_callback_start_test_button(callback_query: types.CallbackQuery, state: FSMContext):
    await states.Form.answer.set()
    test = await tests.get_test([])

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in test.get('answers'):
        keyboard.add(name.get('var'))

    mess = """
        Вопрос: {}
        \nОтветы: \n{}
        """.format(test.get('question').get('text'),
                   '\n'.join((answer.get('answer') for answer in test.get('answers'))))

    await callback_query.message.reply(mess, reply_markup=keyboard)

    await state.update_data(q1={'id': test.get('question').get('id'), 'var': ''})


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    async with state.proxy() as data:
        right, wrong, total = await logics.calculate_score(dict(data))
        await message.answer(messages.test_score_message.format(total, right, wrong))
        await state.finish()

    await state.finish()
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=states.Form.answer)
async def process_gender(message: types.Message, state: FSMContext):
    test = await tests.get_test([])
    state_dict = dict(await state.get_data())
    last = list(state_dict.keys())[-1].split('q')[1]

    async with state.proxy() as data:
        data['q{}'.format(last)]['var'] = message.text
        if int(last) == 2:
            right, wrong, total = await logics.calculate_score(dict(data))
            await message.answer(messages.test_score_message.format(total, right, wrong),
                                 reply_markup=types.ReplyKeyboardRemove())
            await state.finish()
            return
        data['q{}'.format(int(last) + 1)] = {'id': test.get('question').get('id'), 'var': ''}

    await states.Form.answer.set()

    mess = """
            Вопрос: {}
            \nОтветы: \n{}
            """.format(test.get('question').get('text'),
                       '\n'.join((answer.get('answer') for answer in test.get('answers'))))
    await message.answer(mess)
