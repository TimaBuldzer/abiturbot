SECRET_KEY = '0-slckcp=*2r3z7gsemkmj8+f-is+huz$jy@2xtrrewn7kp--f'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd9d0shpr7gmgrn',
        'USER': 'yuauvfomqaioyt',
        'PASSWORD': '3a21ee9550470e853baa27842d16aa8ade342d4f2f1ad6727e3a23367a9587d5',
        'HOST': 'ec2-18-235-107-171.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

WEBHOOK_HOST = 'http://127.0.0.1:8000/'
WEBHOOK_PATH = '/api/v1/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 8000

from .base import *
import django_heroku

django_heroku.settings(locals())
