# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code

from .default import *

"""
It is local version of settings.py for particular developer, stage, production
or test environment here You can overwrite or update apps/settings/default.py's
If it is settings/local.py, it SHOULDN'T be under version control!
"""

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = (
    "localhost.com",
    "localhost"
)

SECRET_KEY = '3ee655f6eb8eb559874e525da3f31969'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': projectpath('') + 'dev.db',  # pylint: disable=undefined-variable
    }
}

# debug_toolbar
# INSTALLED_APPS += ('debug_toolbar',)
# MIDDLEWARE_CLASSES += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# )
# INTERNAL_IPS = ('127.0.0.1',)
# DEBUG_TOOLBAR_PANELS = (
#     'debug_toolbar.panels.version.VersionDebugPanel',
#     'debug_toolbar.panels.timer.TimerDebugPanel',
#     'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#     'debug_toolbar.panels.headers.HeaderDebugPanel',
#     'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
#     'debug_toolbar.panels.template.TemplateDebugPanel',
#     'debug_toolbar.panels.sql.SQLDebugPanel',
#     'debug_toolbar.panels.signals.SignalDebugPanel',
#     'debug_toolbar.panels.logger.LoggingPanel',
# )
# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS' : False
# }
