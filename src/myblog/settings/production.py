import django_heroku

from .base import *


DEBUG = False

try:
    from .local import *
except ImportError:
    print("It's good if you are seeing this error on production.")
    pass

ALLOWED_HOSTS = [
    'aasimkhan.in',
    'aasimkhan-in.herokuapp.com'
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USERNAME"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT", 5432),
    }
}

django_heroku.settings(locals())
