from django.db import models
from datetime import timedelta
from django.db.models import Count
from django.contrib.auth.models import User

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist_profile')
    name = models.CharField('Имя артиста / группы', max_length=100)
    bio = models.TextField(verbose_name='Описание артиста / группы')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name
 
class Album(models.Model):
    title = models.CharField('Название Альбома', max_length=100)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
    )
    image = models.FileField(upload_to='images/album/',verbose_name='Обложка альбома')
    release_date = models.DateField('Дата выхода')

    class Meta:
        ordering = ['artist']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__ (self):
            return self.title

class Song(models.Model):
    title = models.CharField('Название песни',max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,verbose_name='Исполнитель')
    album = models.ForeignKey(Album, on_delete=models.CASCADE,verbose_name='Альбом', related_name='songs')
    # audio_file = models.FileField(upload_to='audio_files/')
    duration = models.DurationField('Длительность',default=timedelta(minutes=0))
    track_number = models.PositiveIntegerField('Номер песни в альбоме', blank=True, null=True)

    class Meta:
        unique_together = ('album','track_number')
        ordering = ['album', 'track_number']
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def __str__ (self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.track_number:
            next_track_number = Song.objects.filter(album=self.album).aggregate(
                next_track_number=Count('id')
            )['next_track_number'] + 1
            self.track_number = next_track_number
        super().save(*args, **kwargs)