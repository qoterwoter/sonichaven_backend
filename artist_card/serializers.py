from rest_framework import serializers
from .models import Song, Album, Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','artist','duration',]

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Album
        fields = ['title', 'artist', 'image', 'release_date', 'songs']

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'image', 'release_date']