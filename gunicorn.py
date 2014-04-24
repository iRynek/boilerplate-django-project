def __create_projectpath(thefile):
    """
    Creates/returns OS-independent projectpath function, starting in basedir of thefile
    """
    from os.path import join, dirname, abspath
    root = abspath(dirname(abspath(thefile)))
    return lambda *a: join(root, *(a + ('',)))
projectpath = __create_projectpath(__file__)

# probably not to change
workers = 2
max_request = 250
forwarded_allow_ips = "*"
chdir = projectpath('')
accesslog = projectpath('log') + 'access.log'
errorlog = projectpath('log') + 'error.log'
raw_env = ['DJANGO_SETTINGS_MODULE=apps.settings']
