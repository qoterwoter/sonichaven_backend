from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'password']