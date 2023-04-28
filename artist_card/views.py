from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status
from .models import Release, Artist
from .serializers import ArtistSerializer, ReleaseSerializer, ReleasesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Artist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView


class ArtistList(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistDetail(APIView):
    def get_object(self, pk):
        try:
            artist = Artist.objects.get(pk=pk)
            return artist
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        artist = self.get_object(pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    def put(self, request, pk):
        artist = self.get_object(pk)
        serializer = ArtistSerializer(artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        artist = self.get_object(pk)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
