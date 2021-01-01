from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('type', type=str, default='start_bot')

    def handle(self, *args, **options):
        if options['type'] == 'start_bot':
            self.start_bot()

    @staticmethod
    def start_bot():
        exec(open('apps/bot/bot.py').read())
