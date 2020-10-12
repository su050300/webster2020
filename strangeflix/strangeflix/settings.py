"""
Django settings for strangeflix project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
# importing django modules
from pathlib import Path
from decouple import config, Csv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [

    # Pre installed apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd Party installs
    'crispy_forms',

    # Apps defined by us
    'home.apps.HomeConfig',
    'accounts.apps.AccountsConfig',
    'subscribe.apps.SubscribeConfig',
    'transaction.apps.TransactionConfig',
    'provider.apps.ProviderConfig',
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

ROOT_URLCONF = 'strangeflix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '')],
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

WSGI_APPLICATION = 'strangeflix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('ENGINE'),
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# DATA_UPLOAD_MAX_NUMBER_FIELDS= 20000

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# login and logout redirection url
LOGIN_REDIRECT_URL = 'home_page'
LOGOUT_REDIRECT_URL = 'home_page'

# setting user auth model
AUTH_USER_MODEL = config('AUTH_USER_MODEL')

# setting static url and directory
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# setting path for media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Configurations to send email
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)


# Instamojo configurations
from instamojo_wrapper import Instamojo

INSTAMOJO_API_KEY=config('INSTAMOJO_API_KEY')
INSTAMOJO_AUTH_TOKEN=config('INSTAMOJO_AUTH_TOKEN')
INSTAMOJO_PRIVATE_SALT=config('INSTAMOJO_PRIVATE_SALT')

INSTAMOJO_API = Instamojo(api_key=INSTAMOJO_API_KEY,auth_token=INSTAMOJO_AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')



# Firebase configurations
FIREBASE_API_KEY=config('FIREBASE_API_KEY')
FIREBASE_AUTH_DOMAIN=config('FIREBASE_AUTH_DOMAIN')
FIREBASE_DATABASE_URL=config('FIREBASE_DATABASE_URL')
FIREBASE_PROJECT_ID=config('FIREBASE_PROJECT_ID')
FIREBASE_STORAGE_BUCKET=config('FIREBASE_STORAGE_BUCKET')
FIREBASE_MESSAGING_SENDER_ID=config('FIREBASE_MESSAGING_SENDER_ID')
FIREBASE_APP_ID=config('FIREBASE_APP_ID')
FIREBASE_MEASUREMENT_ID=config('FIREBASE_MEASUREMENT_ID')