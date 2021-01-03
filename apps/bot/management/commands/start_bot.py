import random
from django.core.management import BaseCommand

from apps.bot.queries import SubjectTest
from conf import settings
from apps.main import models as main_models
from asgiref.sync import sync_to_async


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.start_bot()

    @staticmethod
    def start_bot():
        from aiogram import executor
        from apps.bot.misc import dp
        from apps.bot import handlers
        executor.start_polling(dp, skip_updates=True)
