from django.core.management import BaseCommand
from conf import settings
from apps.main import models as main_models
from asgiref.sync import sync_to_async


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('type', type=str, default='start_bot')

    def handle(self, *args, **options):
        if options['type'] == 'start_bot':
            self.start_bot()

    @staticmethod
    def start_bot():
        import logging

        from aiogram import Bot, Dispatcher, executor, types

        API_TOKEN = settings.BOT_TOKEN

        logging.basicConfig(level=logging.INFO)

        bot = Bot(token=API_TOKEN)
        dp = Dispatcher(bot)

        @sync_to_async
        def get_question():
            return main_models.Question.objects.first().question

        @dp.message_handler(commands=['start', 'help'])
        async def send_welcome(message: types.Message):
            await message.reply(await get_question())

        @dp.message_handler()
        async def echo(message: types.Message):
            await message.answer(message.text)

        executor.start_polling(dp, skip_updates=True)
