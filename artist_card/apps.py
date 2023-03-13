from django.apps import AppConfig

class ArtistCardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artist_card'

    def ready(self):
        import artist_card.signals