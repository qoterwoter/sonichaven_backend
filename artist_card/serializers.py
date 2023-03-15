from rest_framework import serializers
from .models import Song, Release, Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','artist','duration',]

class ReleaseSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Release
        fields = ['title', 'artist', 'image', 'release_date', 'songs']

class ReleasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['title', 'artist', 'image', 'release_date']