from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Artist
from sonichaven.models import User
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def create_artist(sender, instance, created, **kwargs):
    if created and instance.is_artist:
        Artist.objects.create(user=instance, name=instance.username)

@receiver(post_save, sender=User)
def add_user_to_artist_group(sender, instance, created, **kwargs):
    if created and instance.is_artist:
        artist_group, _ = Group.objects.get_or_create(name='Artist')
        instance.groups.add(artist_group)