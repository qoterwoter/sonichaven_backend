from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status
from .serializers import ArtistSerializer, ReleaseSerializer, ReleaseCRUDSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Artist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .models import Song
from .serializers import SongSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Release
from .serializers import ReleaseSerializer


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


class ReleaseListByArtist(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReleaseSerializer

    def get_queryset(self):
        artist_id = self.kwargs['artist_id']
        return Release.objects.filter(artist_id=artist_id)


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseCRUDSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        release = Release.objects.get(pk=pk)
        title = request.data.get('title', None)
        if title is not None:
            release.title = title
            release.save()
            serializer = self.serializer_class(release)
            return Response(serializer.data, status=200)
        else:
            serializer = self.serializer_class(release, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        release = Release.objects.get(pk=pk)
        serializer = self.serializer_class(release)
        return Response(serializer.data, status=200)

    def destroy(self, request, pk=None):
        release = Release.objects.get(pk=pk)
        release.delete()
        return Response(status=204)


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        song = Song.objects.get(pk=pk)
        serializer = self.serializer_class(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        song = Song.objects.get(pk=pk)
        serializer = self.serializer_class(song)
        return Response(serializer.data, status=200)

    def destroy(self, request, pk=None):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(status=204)


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
