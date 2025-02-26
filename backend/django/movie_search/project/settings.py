"""
Django settings for shows project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import logging
from pathlib import Path
from platform import release

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / "data"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ny_%o6*o(npqht@9oc%2hsxz6upvlwir)cuys5-)-at!7gfibw"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True if os.getenv("DJANGO_DEBUG", "True") == "True" else False
DEBUG = True
ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

ADMINS = [
    ("admin", "admin@example.com"),
]

# Application definition

INSTALLED_APPS = [
    "show.apps.ShowConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "django_celery_beat",  # for storing the Celery beat schedule in the django db.
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["project/templates/"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# PostgreSQL (the default)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "demo_app_django_react",
        "USER": "demo_app_django_react",
        "PASSWORD": "demo_app_django_react",
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": "5432",
    }
}

# MySQL
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "demo_app_django_react",
#         "USER": "demo_app_django_react",
#         "PASSWORD": "demo_app_django_react",
#         "HOST": "localhost",
#         "PORT": "3306",
#     }
# }

# SQLite
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# Caches

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{os.environ.get('REDIS_HOST', '127.0.0.1')}:6379",
    }
}

CACHE_MIDDLEWARE_SECONDS = 10

REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 10
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "./app-static/"
STATICFILES_DIRS = (BASE_DIR / "static/",)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Django Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
}


# Celery
from celery.schedules import crontab

CELERY_TIMEZONE = "Europe/London"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = f"redis://{os.environ.get('REDIS_HOST', 'localhost')}:6379/0"
CELERY_RESULT_BACKEND = f"redis://{os.environ.get('REDIS_HOST', 'localhost')}:6379/0"
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'  # for storing the Celery beat schedule in the django db. (see also show.migrations.0003_setup_scheduled_tasks)
CELERY_BEAT_SCHEDULE = (
    {  # if the database scheduler is used, this schedule must be commented out.
        "doing-some-random-stuff-2": {
            "task": "show.tasks.random_task",
            "schedule": 3600,
        },
        "tell-the-world-something-2": {
            "task": "show.tasks.tell_the_world",
            "schedule": crontab(hour="1"),
            "args": ("*Something*",),
        },
    }
)


# Sentry

sentry_dsn = os.getenv("DJANGO_SENTRY_DSN", None)
sentry_release = os.getenv("DJANGO_SENTRY_RELEASE", "0.0.1")
sentry_environment = os.getenv("DJANGO_SENTRY_ENVIRONMENT", "dev")
sentry_traces_sample_rate = float(os.getenv("DJANGO_SENTRY_TRACES_SAMPLE_RATE", "1.0"))
sentry_default_pii = os.getenv("DJANGO_SENTRY_DEFAULT_PII", 'True') == 'True'
sentry_debug = os.getenv("DJANGO_SENTRY_DEBUG", 'True') == 'True'

logging.warning(f"~~~~ sentry_dsn: {sentry_dsn}")
logging.warning(f"~~~~ sentry_release: {sentry_release}")
logging.warning(f"~~~~ sentry_environment: {sentry_environment}")
logging.warning(f"~~~~ sentry_traces_sample_rate: {sentry_traces_sample_rate}")
logging.warning(f"~~~~ sentry_default_pii: {sentry_default_pii}")
logging.warning(f"~~~~ sentry_debug: {sentry_debug}")

import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=sentry_dsn,
    release=sentry_release,
    environment=sentry_environment,
    traces_sample_rate=sentry_traces_sample_rate,
    send_default_pii=sentry_default_pii,
    debug=sentry_debug,
    _experiments={
        "otel_powered_performance": True,
    },
    # integrations=[
    #     CeleryIntegration(
    #         monitor_beat_tasks=True,
    #     ),
    #     DjangoIntegration(
    #         transaction_style="url",
    #         cache_spans=True,
    #         signals_spans=True,
    #         middleware_spans=True,
    #     ),
    # ],
    # enable_db_query_source=True,
    # db_query_source_threshold_ms=0,
    # attach_stacktrace=True,
    # _experiments={
    #     "attach_explain_plans": {
    #         "explain_cache_size": 1000,
    #         "explain_cache_timeout_seconds": 0,
    #         "use_explain_analyze": True,
    #     }
    # }
)
