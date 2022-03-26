from django.apps import AppConfig


class SupervisoryConfig(AppConfig):
    name = 'supervisory'

    def ready(self):
        import supervisory.signals
