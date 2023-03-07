from django.db import models

class Artist(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Имя артиста / группы', max_length=100)
    bio = models.TextField(verbose_name='Описание артиста / группы')

    class Meta:
        ordering = ['id']
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
            return self.name
    
class Album(models.Model):
    title = models.CharField('Название Альбома', max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Исполнитель')
    image = models.FileField(upload_to='album_images/',verbose_name='Обложка альбома')

    class Meta:
        ordering = ['title']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__ (self):
            return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # audio_file = models.FileField(upload_to='audio_files/')
    length = models.PositiveIntegerField()