from __future__ import unicode_literals

from django.apps import AppConfig


class WebuserConfig(AppConfig):
    name = 'webuser'
    def ready(self):
        import signals
