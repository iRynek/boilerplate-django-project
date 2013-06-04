# -*- coding: utf-8 -*-

from django.conf import settings

def default(request):
    return {
        'PROJECT_HOST':settings.PROJECT_HOST,
    }
