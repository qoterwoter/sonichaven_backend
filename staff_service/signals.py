# myapp/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ShopCart
from artist_card.models import Artist

@receiver(post_save, sender=Artist)
def create_shopcart(sender, instance, created, **kwargs):
    if created:
        ShopCart.objects.create(artist=instance)
