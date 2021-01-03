from aiogram import types
from apps.bot import queries
from apps.bot.misc import dp
from apps.bot import keyboards
from apps.bot import states


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    await states.ContactForm.phone.set()

    await message.answer(
        """
        Привет! 
        \nЭто тестовая версия абитуриентского бота!
        \nПока доступны только тесты по русскому языку.
        \nНажми на кнопку чтобы зарегистрироваться.
        """, reply_markup=keyboards.markup_request_phone)


@dp.message_handler(state=states.ContactForm.phone, content_types=['contact'])
async def register_user(message: types.Message):
    await queries.User().get_or_create_user(
        phone=message.contact.phone_number,
        name=message.contact.first_name,
        tg_id=message.contact.user_id
    )
    await message.answer(
        """
        Привет {}! 
        \nЭто тестовая версия абитуриентского бота!
        \nПока доступны только тесты по русскому языку.
        \nНажми на кнопку чтобы начать проходить тесты.
        """, reply_markup=keyboards.markup_start_test)
