# -*- coding: utf-8 -*-
import os

if not os.path.exists('./local.py'):
    raise ImportError("Copy apps/settings/local-sample.py to apps/settings/local.py before launching server!")
else:
    from .local import *

