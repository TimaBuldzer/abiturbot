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


from .base import *
