"""
These settings are used by the ``manage.py`` command.

With normal tests we want to use the fastest possible way which is an
in-memory sqlite database but if you want to create South migrations you
need a persistant database.

"""
from .test_settings import *  # NOQA

from django.contrib import messages

REQUIRED_APPS = [

]


INSTALLED_APPS = INSTALLED_APPS + REQUIRED_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}

