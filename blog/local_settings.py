from .settings import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgres',
        'NAME': config(' NAME'),
        'HOST': config(' HOST'),
        'PORT': config ('PORT'),
        'PASSWORD': config ('PASSWORD'),
    }
}