from django.apps import AppConfig


class StaffServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff_service'

    def ready(self):
        import staff_service.signals
