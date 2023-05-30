from django.contrib.auth import get_user_model
from rest_framework import serializers
from artist_card.serializers import ArtistSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    profile_image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'profile_image', 'first_name', 'last_name',
                  'is_soundengineer', 'is_artist', 'artist', 'password']
        extra_kwargs = {'username': {'required': False}, 'password': {'required': False}, 'profile_image': {'required': False}}

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            email=validated_data.get('email'),
            is_artist=validated_data.get('is_artist')
        )
        user.is_artist = True
        user.save()
        return user

