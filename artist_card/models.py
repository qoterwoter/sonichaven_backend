from datetime import timedelta
from django.db import models
from django.conf import settings
from .utils import get_playcounts


class Artist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                             limit_choices_to={'is_artist': True})
    name = models.CharField('Имя артиста / группы', max_length=100)
    bio = models.TextField(verbose_name='Описание артиста / группы')
    payment = models.DecimalField('Выплата', max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name

    def update_payment(self):
        total_playcounts = self.song_set.aggregate(models.Sum('playcounts'))['playcounts__sum'] or 0
        self.payment = total_playcounts * 0.04

    # def save(self, *args, **kwargs):
    #     self.update_payment()
    #     super().save(*args, **kwargs)


class Release(models.Model):
    STATUS_CHOICES = [
        ('released', 'Выпущен на площадки'),
        ('awaiting_upload', 'Ожидает выгрузки'),
        ('archived', 'Архивирован'),
        ('in_progress', 'В работе'),
    ]
    TYPE_CHOICES = [
        ('album', 'Альбом'),
        ('mixtape', 'Микстейп'),
        ('ep', 'Епи'),
        ('single', 'Сингл'),
    ]
    title = models.CharField('Название', max_length=100)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,verbose_name='Исполнитель',)
    image = models.CharField(max_length=255, verbose_name='Обложка')
    release_date = models.DateField('Дата выхода')
    type = models.CharField('Тип релиза', max_length=12, choices=TYPE_CHOICES)
    listens = models.PositiveIntegerField('Количество прослушиваний', default=0)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='in_progress')

    class Meta:
        ordering = ['artist']
        verbose_name = 'Релиз'
        verbose_name_plural = 'Релизы'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.listens = self.get_total_listens()
        super().save(*args, **kwargs)

    def get_total_listens(self):
        total_listens = 0
        for song in self.songs.all():
            total_listens += song.playcounts or 0
        return total_listens


class Song(models.Model):
    title = models.CharField('Название песни', max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Исполнитель')
    release = models.ForeignKey(Release, on_delete=models.CASCADE, verbose_name='Релиз', related_name='songs')
    # audio_file = models.FileField(upload_to='audio_files/')
    duration = models.DurationField('Длительность', default=timedelta(minutes=0))
    track_number = models.PositiveIntegerField('Номер песни в релизе', blank=True, null=True)
    playcounts = models.PositiveIntegerField('Количество прослушиваний', blank=True, null=True)
    featuring = models.CharField('При участии', max_length=100, blank=True)

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

        artist_name = self.artist.name
        track_name = self.title
        self.playcounts = get_playcounts(artist_name, track_name)
        super().save(*args, **kwargs)

        artist = self.artist
        artist.update_payment()
