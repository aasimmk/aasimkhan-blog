import django_heroku

from .base import *


DEBUG = False

try:
    from .local import *
except ImportError:
    print("It's okay if you are seeing this warning message on production.")
    pass


SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise EnvironmentError('SECRET IS NOT CONFIGURED.')

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