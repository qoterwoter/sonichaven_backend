from django.db import models
from datetime import timedelta
from django.db.models import Count
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Artist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                             limit_choices_to={'is_artist': True})
    name = models.CharField('Имя артиста / группы', max_length=100)
    bio = models.TextField(verbose_name='Описание артиста / группы')
    profile_image = models.CharField(max_length=255, verbose_name='Аватар')

    class Meta:
        ordering = ['pk']
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Release(models.Model):
    TYPE_CHOICES = [
        ('album', 'Альбом'),
        ('mixtape', 'Микстейп'),
        ('ep', 'Епи'),
        ('single', 'Сингл'),
    ]
    title = models.CharField('Название', max_length=100)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
    )
    image = models.CharField(max_length=255, verbose_name='Обложка')
    release_date = models.DateField('Дата выхода')
    type = models.CharField('Тип релиза', max_length=12, choices=TYPE_CHOICES)

    class Meta:
        ordering = ['artist']
        verbose_name = 'Релиз'
        verbose_name_plural = 'Релизы'

    def __str__(self):
        return self.title


def recalculate_track_numbers(release):
    songs = release.songs.all().order_by('track_number')
    for i, song in enumerate(songs):
        song.track_number = i + 1
        song.save()


class Song(models.Model):
    title = models.CharField('Название песни', max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Исполнитель')
    release = models.ForeignKey(Release, on_delete=models.CASCADE, verbose_name='Релиз', related_name='songs')
    # audio_file = models.FileField(upload_to='audio_files/')
    duration = models.DurationField('Длительность', default=timedelta(minutes=0))
    track_number = models.PositiveIntegerField('Номер песни в релизе', blank=True, null=True)

    class Meta:
        unique_together = ('release', 'track_number')
        ordering = ['release', 'track_number']
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.track_number:
            next_track_number = Song.objects.filter(release=self.release).aggregate(
                next_track_number=models.Count('id')
            )['next_track_number'] + 1
            self.track_number = next_track_number
        super().save(*args, **kwargs)
        recalculate_track_numbers(self.release)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        recalculate_track_numbers(self.release)
