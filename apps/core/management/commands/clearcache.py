from django.core.management.base import BaseCommand
from django.core.cache import cache

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """
            Management command clearing the cache
        """
        cache.clear()
