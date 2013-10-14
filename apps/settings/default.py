# -*- coding: utf-8 -*-

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
     'discover_runner',
     'discover_jenkins',

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
# discover_runner
TEST_RUNNER = 'discover_jenkins.runner.DiscoverCIRunner'
TEST_PROJECT_APPS = (
    'apps',
)
TEST_TASKS = (
    'discover_jenkins.tasks.run_pylint.PyLintTask',
)
TEST_PYLINT_RCFILE = projectpath('tests') + 'pylint.rc'  # pylint: disable=undefined-variable

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
# APPS SETTINGS #########################################
