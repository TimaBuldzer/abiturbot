import logging
import conf.settings as settings
from aiogram import Bot, Dispatcher, executor, types

from apps.main.models import Question

API_TOKEN = settings.BOT_TOKEN
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message)


executor.start_polling(dp, skip_updates=True)
