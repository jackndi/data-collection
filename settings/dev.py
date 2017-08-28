from .base import *

SECRET_KEY = '15ebbb9be7694f4848**^*24b800436772b39409*^+'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ENVIRONMENT_NAME = "Duka Connect Development Server"

ENVIRONMENT_COLOR = "#660000"
