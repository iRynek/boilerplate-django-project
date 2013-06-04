boilerplate-django-project
=================

boilerplate-django-project is an attempt to set up a standard convention for django projects
layouts, to assist in writing utilities to deploy such applications.

Related projects
-----------

* jqb's [boilerplate](https://github.com/jqb/boilerplate) - utility to manage boilerplates
* jqb's [boilerplate-django-project](https://github.com/jqb/boilerplate-django-project) 
- jqb's django-project boilerplate


Directory structure
=================

apps
-----------

All of your Django "apps" go in this directory. These have models, views, forms,
templates or all of the above. These should be Python packages you would add to
your project's ``INSTALLED_APPS`` list.

There's one predefined app: ``core``. Every base classes should be placed here.
It's also a place to keep your project-level static files. Here's how you might
to organize it:

  apps/core/static/core/      <== application's css, js, img
  apps/core/static/core/lib/  <== css, js libraries eg. boilerplate

Why is that?

When ``collectstatic`` commands creates the content of ``static`` folder it just
copy contents of static folders from each app. We decide that the best way
to keep clean, resonable and simple structure, will be keeping all static
dependentcies to ``core`` app.

Since django>=1.5 we treat this folder as a main container -- ``apps`` is default
name of project (that's why it is module apps/__init__.py).

lib
-----------

Third party Python packages and/or django-apps. Everything in this directory
is added to the ``PYTHONPATH`` when the ``setup`` function from  ``env.py``
is invoked or ``python manage.py runserver`` is run.

log
-----------

Default place to store logs from your loggers. We recommend ./log/$app/ for keeping logs of $app django application.

static
-----------

This folder is fully auto-generated. You don't even need to create it.
It will be created by ``python manage.py collectstatic`` command line tool.

req
-----------

Folder for pip requirements files, optionally one for each environment. The
``common.txt`` is installed in every case. Additionaly packages.txt
contains information about specific system package distribution eg. apt-get for debian.

apps/settings
-----------

Settings which enable distinction between default and local scope. Each environment 
gets it's own ``apps/settings/local.py`` which IS NOT shared across CVS.
Only default.py should be placed there. Settings from default.py are covered by each
environment local.py versions.

We provide ``local-dev-sample.py`` which is project settings boilerplate to start with,
just copy it to ``apps/settings/local.py`` and You are ready to go!

Additionaly we think that urls.py fit in here nicely.


Files
=================

env.py
-----------

Introduces ``setup`` function that modifies the ``PYTHONPATH`` to allow importing
from the ``lib`` directories. It also provide WSGI application interface.
Just point dir of WSGI to ``/boilerplate-django-project/`` and give ``env`` as a module.

manage.py
-----------
The standard Django ``manage.py``.


Authors
=================

* [Kuba Janoszek](https://github.com/jqb/)
* [Leszek Piątek](https://github.com/lechup/)
