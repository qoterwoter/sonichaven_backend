from django.contrib import admin

from .models import Song, Album, Artist

admin.site.register(Song)

class AlbumAdmin(admin.ModelAdmin):
    model = Album
    list_display = ('title', 'artist')

    def get_songs(self,obj):
        return obj.song.title

admin.site.register(Album, AlbumAdmin)

admin.site.register(Artist)

# Register your models here.
