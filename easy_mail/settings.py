"""
Django settings for easy_mail project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from os import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-er1rvq7ve&_)j0yok)b9wj8ag&=4no&m__+@@kg5c&#ma5w%2%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# CORS
CORS_ALLOW_ALL_ORIGINS = environ.get("CORS_ALLOW_ALL_ORIGINS", "false").lower() == "true"
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    *environ.get("ALLOWED_ORIGINS_FE", "http://127.0.0.1:5173|http://localhost:5173").split("|"),
    *environ.get("ALLOWED_ORIGINS_BE", "http://127.0.0.1:8000|http://localhost:8000").split("|"),
]

CSRF_COOKIE_NAME = "csrftoken"
CSRF_HEADER_NAME = "CSRF_COOKIE"
CSRF_TRUSTED_ORIGINS = [
    *environ.get("ALLOWED_ORIGINS_FE", "http://127.0.0.1:5173|http://localhost:5173").split("|"),
    *environ.get("ALLOWED_ORIGINS_BE", "http://127.0.0.1:8000|http://localhost:8000").split("|"),
]

SESSION_COOKIE_SECURE = environ.get("SESSION_COOKIE_SECURE", "false").lower() == "true"
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE
CSRF_COOKIE_HTTPONLY = False
if CSRF_COOKIE_SECURE:
    CSRF_COOKIE_SAMESITE = None
else:
    CSRF_COOKIE_SAMESITE = "Lax"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_spectacular',
    
    'src.accounts',
    'src.inbox',
    'src.contacts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'easy_mail.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'easy_mail.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#DRF
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # "DEFAULT_FILTER_BACKENDS": [
    #     "django_filters.rest_framework.DjangoFilterBackend"
    # ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 50
}

#SEPCTACULAR
SPECTACULAR_SETTINGS = {
    'TITLE': 'Learning Games For Kids API',
    'DESCRIPTION': 'API for learning games for kids',
    'VERSION': '1.0.0',
    'SCHEMA_PATH_PREFIX': '/api',
}
