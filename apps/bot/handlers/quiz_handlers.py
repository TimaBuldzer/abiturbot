from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from asgiref.sync import sync_to_async

from apps.bot.queries import SubjectTest
from apps.bot.misc import dp

tests = SubjectTest()


@dp.callback_query_handler(lambda c: c.data == 'start_test')
async def process_callback_start_test_button(callback_query: types.CallbackQuery):
    await callback_query.answer('Нажата первая кнопка!')

#
# @dp.message_handler(commands='start')
# async def cmd_start(message: types.Message, state: FSMContext):
#     """
#     Conversation's entry point
#     """
#     # Set state
#     await Form.answer.set()
#     test = await get_test([])
#
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for name in test.get('answers'):
#         keyboard.add(name.get('var'))
#
#     mess = """
#     Вопрос: {}
#     \nОтветы: \n{}
#     """.format(test.get('question').get('text'),
#                '\n'.join((answer.get('answer') for answer in test.get('answers'))))
#
#     await message.reply(mess, reply_markup=keyboard)
#
#     async with state.proxy() as data:
#         data['question'] = test.get('question').get('id')
#
#
# # You can use state '*' if you need to handle all states
# @dp.message_handler(state='*', commands='cancel')
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
# async def cancel_handler(message: types.Message, state: FSMContext):
#     """
#     Allow user to cancel any action
#     """
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#
#     await state.finish()
#     await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())
#
#
# @dp.message_handler(state=Form.answer)
# async def process_gender(message: types.Message, state: FSMContext):
#     test = await get_test([])
#
#     async with state.proxy() as data:
#         print(data)
#         data['answer'] = message.text
#         data['question'] = test.get('question').get('id')
#
#     await Form.answer.set()
#     await message.reply(test.get('question').get('text'))
#
#     print(data)
#     # Finish conversation
#     # await state.finish()
