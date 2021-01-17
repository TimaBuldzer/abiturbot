from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup

from apps.bot import states, logics, messages
from apps.bot.queries import SubjectTest
from apps.bot.misc import dp
from apps.bot import keyboards, test_categories


@dp.message_handler(lambda msg: 'тесты' in msg.text.lower(), state='*')
async def process_test_categories(message: types.Message):
    await message.answer('Выберите нужную вам категорию', reply_markup=keyboards.markup_test_categories)


@dp.message_handler(lambda msg: msg.text in test_categories.categories)
async def process_callback_start_test_button(message: types.Message, state: FSMContext):
    tests = SubjectTest(message.text)

    await states.Form.answer.set()
    test = await tests.get_test([])
    if not test:
        await message.answer('Сорри, вопросов по этой категории пока нету. Выберите другую.')

        await state.finish()

        return

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=5).add(
        *[name.get('var') for name in test.get('answers')]).add('Отмена')

    await message.answer(await tests.cast_to_string(test), reply_markup=keyboard)

    await state.update_data(q1={'id': test.get('question').get('id'), 'var': ''})
    await state.update_data(category=message.text)


@dp.message_handler(lambda msg: msg.text == 'Отмена', state='*')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    async with state.proxy() as data:
        data.pop('category')
        right, wrong, total = await logics.calculate_score(dict(data))
        await message.answer(messages.test_score_message.format(total, right, wrong),
                             reply_markup=keyboards.markup_menu)
        await state.finish()

    await state.finish()
    await message.reply('Отменено.', reply_markup=keyboards.markup_menu)


@dp.message_handler(state=states.Form.answer)
async def process_gender(message: types.Message, state: FSMContext):
    total_tests = 30

    async with state.proxy() as data:
        category = data.pop('category')

    tests = SubjectTest(category)

    test = await tests.get_test([])
    state_dict = dict(await state.get_data())
    last = list(state_dict.keys())[-1].split('q')[1]

    async with state.proxy() as data:
        data['q{}'.format(last)]['var'] = message.text
        if int(last) == total_tests:
            right, wrong, total = await logics.calculate_score(dict(data))
            await message.answer(messages.test_score_message.format(total, right, wrong),
                                 reply_markup=keyboards.markup_menu)
            await state.finish()

            return
        data['q{}'.format(int(last) + 1)] = {'id': test.get('question').get('id'), 'var': ''}

    await states.Form.answer.set()

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=5).add(
        *[name.get('var') for name in test.get('answers')]).add('Отмена')

    await message.answer(await tests.cast_to_string(test), reply_markup=keyboard)

    await state.update_data(category=category)
