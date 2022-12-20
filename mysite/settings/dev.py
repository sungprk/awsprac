from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-lr4#ww^sfgbsxbti%!&0g-fxi3!-3vgd(o&j+ygon2c6^cy$&="

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [".eu-west-1.compute.amazonaws.com"]

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
