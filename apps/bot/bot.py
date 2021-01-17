from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
from conf.settings import WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT

from aiogram import executor, types
from apps.bot.misc import dp, bot
from apps.bot.handlers import *

executor.start_polling(dp, skip_updates=True)


def telegram_bot_start(request):
    print(request)


@dp.message_handler()
async def echo(message: types.Message):
    return SendMessage(message.chat.id, message.text)


async def on_startup(d):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(d):
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
