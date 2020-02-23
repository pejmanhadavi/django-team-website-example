from ._base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bz=mg6b!@)h0m*r=cycj4r4^r!1$7(xogpp!w=zj%4+u^pbg!7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}