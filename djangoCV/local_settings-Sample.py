# Edit this file and save as local_settings.py

SECRET_KEY = 'secret_key_string'

ALLOWED_HOSTS = ['ip', '.domain.tld']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'database_user',
        'PASSWORD': 'database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}