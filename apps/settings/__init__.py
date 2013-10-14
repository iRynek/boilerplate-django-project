# -*- coding: utf-8 -*-
"""
Module which load settings/default.py settings, and than overwrites those with
settings/local.py. Additionally we add projectpath() method to be used in
default.py and local.py and we add projectpath('lib') to PYTHONPATH
"""

import os
import sys

def create_projectpath(thefile):
    from os.path import join, dirname, abspath
    root = abspath(join(dirname(abspath(thefile)), '..', '..'))
    return lambda *a: join(root, *(a + ('',)))

# "Temporary globals" that might be useful
# It can be used in each settings file as built-in
projectpath = create_projectpath(__file__)

# sequence of settings module to read
files_base_names = [
    'default',
    'local'
]

for file_base_name in files_base_names:
    filepath = os.path.join(
        projectpath('apps', 'settings'),
        '%s.py' % file_base_name
    )
    # That is kind of hacky but file path is generated from
    # static defined variables. If someone get's right to
    # overwrite your local or default'pys You are already
    # screwed ;)
    if os.path.exists(filepath):
        execfile(filepath)

# Setup PYTHOPATH - add projectpath('lib') before any others paths
# overwrite django and other shared Python libs
# it's one of 'little ugly hack' that make things works
if os.path.exists(projectpath('lib')) and len(sys.path) > 0 and sys.path[0] is not projectpath('lib'):
    sys.path.insert(0, projectpath('lib'))

# cleanup
del files_base_names, projectpath, create_projectpath
