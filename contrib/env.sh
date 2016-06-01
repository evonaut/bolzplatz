# Environment variables required by the Django application at runtime.
# May be added to the virtualenv's activate script.
#
# Keep the production file outside of version control!

export DJANGO_SETTINGS_MODULE='config.settings.prod'

export BOLZPLATZ_SECRET_KEY="Super Secure Django Secret Key"
export BOLZPLATZ_DB_NAME='bolzplatz'
export BOLZPLATZ_DB_USER='bolzplatz'
export BOLZPLATZ_DB_PASSWORD='Super Secure Database Password'