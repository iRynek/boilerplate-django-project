# -*- coding: utf-8 -*-
from fabric.api import task, run, env
from fabric.context_managers import cd

####################
## CONFIG
env.project_root = '~/web/'
env.activate_virtual_env = 'source ~/.ve/bin/activate'
env.hosts = ['user@example.com:22']
env.roledefs = {
    'web': env.hosts,
}

@task
def deploy():
    pull_repo()        # pull code from repository
    install_reqs()     # install requirements in virtualenv
#    migrate()         # migrate database if using south
#    syncdb()          # sync db if using one but not south
    load_common_data() # load common data just like initial_data,
                       # but loaded always not only on initial syncdb/migrate
    collectstatic()    # collect your static files
    restart()          # restart web server
    clearcache()       # clear cache which might be in use

## CONFIG END
####################

def virtualenv(command):
    return run(env.activate_virtual_env + ' && ' + command)

@task
def clearcache():
    with cd(env.project_root):
        virtualenv(u'python manage.py clearcache')

@task
def load_common_data():
    with cd(env.project_root):
        virtualenv(u'python manage.py loaddata common_data')

@task
def pull_repo():
    with cd(env.project_root):
        run(u'git pull')

@task
def collectstatic():
    with cd(env.project_root):
        virtualenv(u'python manage.py collectstatic --noinput')

@task
def migrate():
    with cd(env.project_root):
        virtualenv(u'python manage.py migrate')

@task
def syncdb():
    with cd(env.project_root):
        virtualenv(u'python manage.py syncdb')

@task
def restart():
    with cd(env.project_root):
        run(u'touch uwsgi.xml')

@task
def install_reqs():
    with cd(env.project_root):
        virtualenv(u'pip install -r reqs/pip.txt')
