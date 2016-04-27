from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_env_variable('BOLZPLATZ_DB_NAME'),
        "USER": get_env_variable('BOLZPLATZ_DB_USER'),
        "PASSWORD": get_env_variable('BOLZPLATZ_DB_PASSWORD'),
        "HOST": "localhost",
        "PORT": "",
    }
}

INSTALLED_APPS += ("debug_toolbar",)