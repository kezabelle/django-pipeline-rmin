# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import os

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'TESTTESTTESTTESTTESTTESTTESTTEST')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,testserver').split(',')
BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'pipeline',
]

PIPELINE = {
    'STYLESHEETS': {
        'global': {
            'source_filenames': (
            ),
            'output_filename': 'css/global_bundled.css',
        }
    },
    'CSS_COMPRESSOR': 'rmin.RCSSMinCompressor',
    'JAVASCRIPT': {
        'global': {
            'source_filenames': (
            ),
            'output_filename': 'css/global_bundled.js',
        }
    },
    'JS_COMPRESSOR': 'rmin.RJSMinCompressor'
}


SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False

STATIC_URL = '/__static__/'
MEDIA_URL = '/__media__/'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_HTTPONLY = True

ROOT_URLCONF = 'test_urls'

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = (
)
TEMPLATE_LOADERS = (
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]

MIDDLEWARE_CLASSES = (
)

STATIC_ROOT = os.path.join(BASE_DIR, 'test_collectstatic')
MEDIA_ROOT = os.path.join(BASE_DIR, 'test_media')

USE_TZ = True
SILENCED_SYSTEM_CHECKS = ['1_8.W001']
