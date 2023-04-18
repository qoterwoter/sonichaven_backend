from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import UserManager as BaseUserManager


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_artist', False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        if user.is_artist:
            artist_group, _ = Group.objects.get_or_create(name='Artist')
            user.groups.add(artist_group)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    is_soundengineer = models.BooleanField('Статус звукорежиссера', default=False)
    is_artist = models.BooleanField('Статус артиста', default=False)
    # add related_name argument to resolve clashes with reverse relation names
    groups = models.ManyToManyField(Group, blank=True, related_name='users_in_group')

    objects = UserManager()

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='users_with_permission',
        verbose_name=('user permissions'),
        help_text=(
            'Specific permissions for this user.'),
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
