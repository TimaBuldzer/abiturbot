from aiogram import types
from apps.bot.misc import dp
from apps.bot import states, queries, keyboards, messages


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    await states.ContactForm.phone.set()

    await message.answer(messages.start_message, reply_markup=keyboards.markup_request_phone)


@dp.message_handler(state=states.ContactForm.phone, content_types=['contact'])
async def register_user(message: types.Message):
    await queries.User().get_or_create_user(
        phone=message.contact.phone_number,
        name=message.contact.first_name,
        tg_id=message.contact.user_id
    )
    await message.answer(
        messages.register_user_message.format(message.contact.first_name),
        reply_markup=keyboards.markup_start_test
    )
