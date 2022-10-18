from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "necipmuzaffer@gmail.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Dapp"

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
    }
}


# CELERY_BROKER_URL = env("CELERY_BROKER")
# CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
# CELERY_TIMEZONE = "Europe/Istanbul"