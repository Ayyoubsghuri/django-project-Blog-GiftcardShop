"""
Django settings for Lux project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
#matnsach tdir os
import os
from pathlib import Path
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^dgq=#whmr=)#bruztlce2%9&t$2bu1#o+4l9tv0%p@6b%^m89'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'shop.apps.ShopConfig',
    'blog.apps.BlogConfig',
    'zearch.apps.ZearchConfig',
    'user.apps.UserConfig',
    'widget_tweaks',
    'froala_editor',
    'whitenoise.runserver_nostatic',
# hado li lfo9 apps li zdt
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Lux.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # blasa fen tdir templates
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',

            ],
        },
    },
]

WSGI_APPLICATION = 'Lux.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'static')
# hadi li lfo9 tatkhli dossi ywli par default gha mwd3 dyalo
STATIC_URL = '/static/'
# hadi li lt7t tatkhli tat7t ga3 dossyat f memory dyal systeme
STATICFILES_DIRS=[
   os.path.join(BASE_DIR,'lux/static')
]

# if DEBUG:
#     STATICFILES_DIRS=[os.path.join(BASE_DIR,'lux/static')]
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR,'static')



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'user.CustomUser' # new
AUTHENTICATION_BACKENDS = ['user.backends.EmailBackend'] # new

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# LOGIN_REDIRECT_URL = '/logout'

FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
        'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image', 'inline_style',
        'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
        'url', 'video')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/media/')
FROALA_UPLOAD_PATH='static/media/'


LOGIN_REDIRECT_URL ='user:index'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'



EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='email.molchi@gmail.com'
EMAIL_HOST_PASSWORD='accounts.google'


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))

import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
django_heroku.settings(locals())