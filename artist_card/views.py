from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .models import Song, Album, Artist
from .serializers import ArtistSerializer, AlbumSerializer, AlbumsSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AlbumAPIView(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AlbumsAPIView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]