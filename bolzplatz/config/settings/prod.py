from .base import *

DEBUG = False

# Email
# https://docs.djangoproject.com/en/1.8/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SERVER_EMAIL = 'contact@bolzplatz.tips'
DEFAULT_FROM_EMAIL = 'no-reply@bolzplatz.tips'
EMAIL_SUBJECT_PREFIX = '[Bolzplatz] '
MANAGERS = (
    ('Us', 'ourselves@bolzplatz.tips'),
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
