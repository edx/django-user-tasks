"""
These settings are here to use during tests, because django requires them.

In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""

from __future__ import absolute_import, unicode_literals

import tempfile
from os.path import abspath, dirname, join

from celery import Celery

app = Celery('user_tasks')
app.config_from_object('django.conf:settings')


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)


AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

BROKER_URL = 'memory://localhost/'
CELERY_IGNORE_RESULT = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'rest_framework',
    'user_tasks.apps.UserTasksConfig',
)

LOCALE_PATHS = [
    root('user_tasks', 'conf', 'locale'),
]

MEDIA_ROOT = tempfile.mkdtemp()

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'test_urls'

SECRET_KEY = 'insecure-secret-key'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    }
]

USE_TZ = True
