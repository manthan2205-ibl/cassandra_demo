"""
Django settings for cassandra_demo project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from logging import FATAL
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c6b93o&ux3dueq3&=wtv8fkp7(g@l%^fl6a(409)$rybb-2d7w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'django_cassandra_engine',
    'app',
    'rest_framework',
    # 'django_cassandra_engine.sessions',
    
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

ROOT_URLCONF = 'cassandra_demo.urls'

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

WSGI_APPLICATION = 'cassandra_demo.wsgi.application'
ASGI_APPLICATION = 'cassandra_demo.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

REST_FRAMEWORK = {
    # 'DATETIME_INPUT_FORMATS': ['%Y-%m-%d%H:%M:%S%z',],
    # 'DATE_INPUT_FORMATS': [("%Y-%m-%d"),],

    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'app.authentication.MyOwnTokenAuthentication',
    # ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    # 'DEFAULT_PAGINATION_CLASS': 'app.utils.CustomPagination',
    # 'PAGE_SIZE': 3,
    'EXCEPTION_HANDLER': 'app.utils.custom_exception_handler'
}



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# keyspaces

CASSANDRA_FALLBACK_ORDER_BY_PYTHON = True

from cassandra import ConsistencyLevel
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
        'cassandra': {
            'ENGINE': 'django_cassandra_engine',
            'NAME': 'tutorialspoint',
            'USER': 'cassandra',
            'PASSWORD': 'cassandra',
            'TEST_NAME': 'test_db',
            'HOST': '127.0.0.1',
            'OPTIONS': {
                'replication': {
                    'strategy_class': 'SimpleStrategy',
                    # NetworkTopologyStrategy
                    'replication_factor': 1
                },
                'connection': {
                    'consistency': ConsistencyLevel.LOCAL_ONE,
                    # QUORUM
                    'retry_connect': True
                    # + All connection options for cassandra.cluster.Cluster()
                },
                'session': {
                    'default_timeout': 10,
                    'default_fetch_size': 10000
                    # + All options for cassandra.cluster.Session()
                }
            }
        }
    }


# SESSION_ENGINE = 'django_cassandra_engine.sessions.backends.db'


# DATABASES = {
#         'default': {
#             'ENGINE': 'django_cassandra_engine',
#             'NAME': 'db_name',
#             'TEST_NAME': 'db_name',
#             'USER': 'username',
#             'PASSWORD': 'password',
#             'HOST': '0e14d33e-6547-44d2-8089-3ccf94c4faaf-ap-southeast-1.apps.astra.datastax.com',
#             'OPTIONS': {
#                 'connection': {
#                     'cloud': {
#                         'secure_connect_bundle': 'D:/laptop/company/IBL infotech/topics/cassandra/secure-connect-cassandra-demo.zip'
#                     },
#                 }
#             }
#         }
#     }


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
import os
STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR,'static')
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bhavsarmanthan10@gmail.com'
EMAIL_HOST_PASSWORD = 'manthan2205'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
