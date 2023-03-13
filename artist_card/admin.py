from django.contrib import admin
from .models import Song, Album, Artist
from django import forms
from django.contrib.auth.admin import UserAdmin

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get the current artist ID from the request
        artist_id = self.initial.get('artist')
        if artist_id:
            # Filter the available albums based on the current artist
            self.fields['album'].queryset = Album.objects.filter(artist_id=artist_id)



class SongAdmin(admin.ModelAdmin):
    form = SongForm
    list_display = ('title','artist','album','duration')
    list_filter = ['artist','album']
    search_fields = ('title','artist__name','album__title')

admin.site.register(Song, SongAdmin)

class AlbumAdmin(admin.ModelAdmin): 
    list_display = ('title', 'artist','release_date')
    list_filter = ['artist']
    search_fields = ('title', 'artist__name')

admin.site.register(Album, AlbumAdmin)


# class ArtistAdmin(UserAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'name', 'bio')

# admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artist)

# Register your models here.
