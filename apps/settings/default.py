# -*- coding: utf-8 -*-

#####################################
### UTILS
import os
import sys

# "Temporary globals" that might be useful
# It can be used in each settings file as built-in
def __create_projectpath(thefile):
    from os.path import join, dirname, abspath
    root = abspath(join(dirname(abspath(thefile)), '..', '..'))
    return lambda *a: join(root, *(a + ('',)))
projectpath = __create_projectpath(__file__)

# Setup PYTHOPATH - add projectpath('lib') before any others paths
# overwrite django and other shared Python libs
# it's one of 'little ugly hack' that make things works
if os.path.exists(projectpath('lib')) and len(sys.path) > 0 and sys.path[0] is not projectpath('lib'):
    sys.path.insert(0, projectpath('lib'))

####################################
### UTILS END

####################################
### SETTINGS DEFAULT
### set Your version of variables in local.py
### if You do not have one, copy local-sample.py

# set SECRET_KEY in local.py to avoid
# distributing it along in your CVS
SECRET_KEY = ''

PROJECT_ROOT = projectpath()

ROOT_URLCONF = 'apps.settings.urls'
TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'pl'

DEBUG = False
TEMPLATE_DEBUG = False
ADMINS = ()
MANAGERS = ()

USE_I18N = False
USE_L10N = False

INSTALLED_APPS = (
     # ## CONTRIB
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     # ## INTERNAL
    'apps.core',
     # ## EXTERNAL via ./lib/
     # ## EXTERNAL via VIRTUALENV
     'south',
     'compressor',

)
TEMPLATE_LOADERS = (('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',

    'apps.core.context_processors.default',
)

# APPS SETTINGS #########################################
# django.contrib.sites
SITE_ID = 1

# django.contrib.admin
ADMIN_MEDIA_PREFIX = '/static/admin/'

# django.contrib.staticfiles
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
STATIC_ROOT = projectpath('static')
STATIC_URL = '/static/'

MEDIA_ROOT = projectpath('media')
MEDIA_URL = '/media/'

# django_compressor
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc -x --clean-css {infile}'),
)
# APPS SETTINGS #########################################
