from django.contrib.auth import get_user_model
from rest_framework import serializers
from artist_card.serializers import ArtistSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_soundengineer', 'is_artist', 'artist']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
