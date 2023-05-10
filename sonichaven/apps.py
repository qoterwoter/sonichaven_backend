from django.apps import AppConfig


class SonicHavenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sonichaven'

    def ready(self):
        import sonichaven.signals
