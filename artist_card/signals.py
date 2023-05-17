from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Artist

User = get_user_model()


@receiver(post_save, sender=User)
def create_artist_profile(sender, instance, created, **kwargs):
    if created and instance.is_artist:
        artist = Artist(user=instance, name=instance.username)
        artist.save()


# @receiver(post_save, sender=User)
# def assign_user_to_artist_group(sender, instance, created, **kwargs):
#     if created and instance.is_artist:
#         artist_group = Group.objects.get(name='Artist')
#         instance.groups.add(artist_group)