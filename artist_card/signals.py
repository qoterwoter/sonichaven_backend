from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Artist

User = get_user_model()

@receiver(post_save, sender=User)
def create_artist(sender, instance, created, **kwargs):
    if created and not instance.is_staff and not instance.is_superuser:
        Artist.objects.create(user=instance, name=instance.username)