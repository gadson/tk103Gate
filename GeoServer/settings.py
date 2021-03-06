"""
Django settings for GeoServer project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fgdsu0%=o3$t#&8oz$^hh7yjri^05p@vf*93qz-)&ep5$+vz79'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
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

ROOT_URLCONF = 'GeoServer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'GeoServer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        #SQLight3 настройка
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #Postgress настройка
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
 #   {
 #       'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
 #   },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


#STATICFILES_DIRS = "/home/gadson/GeoServerGoogle/GeoServer/static/"
STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(STATIC_ROOT, 'bootstrap/css'),
                    os.path.join(STATIC_ROOT, 'bootstrap/js'),
                    os.path.join(STATIC_ROOT, 'images'),
                    os.path.join(STATIC_ROOT, 'web/assets/mobirise-icons'),
                    os.path.join(STATIC_ROOT, 'tether'),
                    os.path.join(STATIC_ROOT, 'socicon/css'),
                    os.path.join(STATIC_ROOT, 'dropdown/css'),
                    os.path.join(STATIC_ROOT, 'theme/css'),
                    os.path.join(STATIC_ROOT, 'mobirise/css'),
                    os.path.join(STATIC_ROOT, 'web/assets/jquery'),
                    os.path.join(STATIC_ROOT, 'popper'),
                    os.path.join(STATIC_ROOT, 'dropdown/js'),
                    os.path.join(STATIC_ROOT, 'touchswipe'),
                    os.path.join(STATIC_ROOT, 'parallax'),
                    os.path.join(STATIC_ROOT, 'smoothscroll'),
                    os.path.join(STATIC_ROOT, 'theme/js'),
                    os.path.join(STATIC_ROOT, 'socicon/fonts'),
                    os.path.join(STATIC_ROOT, '/'),
                    )

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#Email sending account settings 
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
FROM_EMAIL=''

#Google GCM PUSH service API key 
GOOGLE_API_KEY = ""

#RocketChat server settings for log messages
RC_USERNAME = 'Robot_Vasia'
RC_PASSWORD = ''
RC_DOMAIN = 'http://*******:3000'

