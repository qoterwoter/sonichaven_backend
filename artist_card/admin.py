from django.contrib import admin
from .models import Song, Album, Artist
from .forms import SongForm
from django.utils.html import format_html_join

class SongAdmin(admin.ModelAdmin):
    form = SongForm
    list_display = ('title','artist','album','duration')
    list_filter = ['artist','album']
    search_fields = ('title','artist__name','album__title')

admin.site.register(Song, SongAdmin)

class SongInline(admin.TabularInline):
    model = Song
    extra = 1
    fields = ('title', 'duration','artist')

    autocomplete_fields = ('artist',)

class AlbumAdmin(admin.ModelAdmin): 
    list_display = ('id','title', 'artist','release_date')
    list_filter = ['artist']
    inlines = [SongInline]
    search_fields = ('title', 'artist__name')
    
admin.site.register(Album, AlbumAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'bio','user')
    search_fields = ('name','bio')

admin.site.register(Artist, ArtistAdmin)
