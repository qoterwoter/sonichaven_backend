from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status
from .models import Release, Artist
from .serializers import ArtistSerializer, ReleaseSerializer, ReleasesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Artist
from rest_framework.decorators import api_view, permission_classes


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ReleaseAPIView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, artist_id):
        releases = Release.objects.filter(artist=artist_id)
        serializer = ReleaseSerializer(releases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReleasesAPIView(generics.ListCreateAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleasesSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def artist_info(request):
    user = request.user
    try:
        artist = user.artist_profile
    except Artist.DoesNotExist:
        return Response({'error': 'Artist profile does not exist.'}, status=404)

    data = {
        'user_id': user.id,
        'artist_id': artist.id,
        'username': user.username,
        'email': user.email,
        'artist_name': artist.name,
        'artist_bio': artist.bio,
    }
    return Response(data)