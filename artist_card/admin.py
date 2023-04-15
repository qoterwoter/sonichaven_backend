from django.contrib import admin
from .models import Song, Release, Artist
from .forms import SongForm
from django.utils.html import format_html_join

class SongAdmin(admin.ModelAdmin):
    form = SongForm
    list_display = ('title','artist','release','duration')
    list_filter = ['artist','release']
    search_fields = ('title','artist__name','release__title')

admin.site.register(Song, SongAdmin)

class SongInline(admin.TabularInline):
    model = Song
    extra = 1
    fields = ('title', 'duration','artist')

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_date')
    list_filter = ['artist']
    inlines = [SongInline]
    search_fields = ('title', 'artist__name')
    can_delete = True

    fieldsets = (
        (None, {
            'fields': ('title', 'artist', 'image', 'release_date', 'type')
        }),
    )



admin.site.register(Release, ReleaseAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'bio','user')
    search_fields = ('name','bio')

admin.site.register(Artist, ArtistAdmin)
