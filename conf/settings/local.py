SECRET_KEY = '0-slckcp=*2r3z7gsemkmj8+f-is+huz$jy@2xtrrewn7kp--f'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'abitur',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

WEBHOOK_HOST = 'http://127.0.0.1:8000/'
WEBHOOK_PATH = '/api/v1/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 8000


from .base import *
