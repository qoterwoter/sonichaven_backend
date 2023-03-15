from django import forms
from .models import Song, Release

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
            self.fields['release'].queryset = Release.objects.filter(artist_id=artist_id)