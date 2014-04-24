import os
import sys


def __create_projectpath(thefile):
    """
    Creates/returns OS-independent projectpath function, starting in basedir of thefile
    """
    from os.path import join, dirname, abspath
    root = abspath(dirname(abspath(thefile)))
    return lambda *a: join(root, *(a + ('',)))
projectpath = __create_projectpath(__file__)


def setup(settings_module_name=None):
    """
    Simple setup snippet that makes easy to create
    fast sandbox to try new things.

    :param settings_module_name: name of settings module eg:
         "project.setting"

    Usage:
    >>> import env
    >>> env.setup()
    >>> # from now on paths are setup, and django is configured
    >>> # you can use it in separate "sandbox" script just to check
    >>> # things really quick
    """

    # add ./lib before any others paths
    # overwrite django and other shared python libs
    # it's one of 'little ugly hack' that make things works
    sys.path.insert(0, projectpath(''))
    if os.path.exists(projectpath('lib')):
        sys.path.insert(0, projectpath('lib'))

    settings_module_name = settings_module_name or 'apps.settings'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module_name)


def application(environ, start_response):
    """
    Used for WSGI servers
    """
    setup()
    from django.core.handlers.wsgi import WSGIHandler
    return WSGIHandler()(environ, start_response)