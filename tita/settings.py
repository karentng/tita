"""
Django settings for tita project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lkl1m_!x$2^5@9l7d1^g2ck18ocu17n7s_o#jha-&au+_0!*ud'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#para login

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_URL = reverse_lazy('logout')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'bootstrap3',
    'datetimewidget',
    'django_select2',
    'django_extensions', # para sqldiff
    'bootstrap3_datetime',

    'convocat',
    #'estudiante',
    'campus',
    'survey',
    #'cronograma',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'tita.urls'

WSGI_APPLICATION = 'tita.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import socket
PRODUCTION_SERVER = socket.gethostname()=='www.titaedpt.com.co'

if PRODUCTION_SERVER:
    DATABASES = {  # NO CAMBIAR!!!
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'titadb',                      
            'USER': 'titausr',
            'PASSWORD': 'A893hj9d#ls',
            'HOST': '10.28.132.1',
        }
    }
else:    # Configuracion desarrollo:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'tita',                      
            'USER': 'tita',
            'PASSWORD': 'tita',
            'HOST': '',
        }
    }



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

#USE_TZ = True

SHORT_DATE_FORMAT = 'Y-m-d'
SHORT_DATETIME_FORMAT = 'Y-m-d'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Plantillas de la aplicacion
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

# Archivos estaticos (js, css, template completo, imagenes, etc)
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static_collected') 


MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
MEDIA_URL = '/media/'

# configuraciones del django_select2
AUTO_RENDER_SELECT2_STATICS = False
SELECT2_BOOTSTRAP = True
