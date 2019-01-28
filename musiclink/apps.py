from django.apps import AppConfig


class MusiclinkConfig(AppConfig):
    name = 'musiclink'

    def ready(self):
        import musiclink.signals
