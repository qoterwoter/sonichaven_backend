from rest_framework import serializers
from .models import Song, Release, Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': False},
            'bio': {'required': False},
            'profile_image': {'required': False},
        }

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'duration', ]


class ReleaseSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Release
        fields = ['title', 'artist', 'image', 'release_date', 'songs']


class ReleasesSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name', read_only=True)

    class Meta:
        model = Release
        fields = ['title', 'artist_name', 'image', 'release_date']
