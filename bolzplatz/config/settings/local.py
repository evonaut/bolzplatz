from .base import *

DEBUG = True

# Email
# https://docs.djangoproject.com/en/1.8/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SERVER_EMAIL = 'contact@fc-bolzplatz.eu'
DEFAULT_FROM_EMAIL = 'no-reply@fc-bolzplatz.eu'
EMAIL_SUBJECT_PREFIX = '[Bolzplatz] '
MANAGERS = (
    ('Us', 'ourselves@fc-bolzplatz.eu'),
)

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