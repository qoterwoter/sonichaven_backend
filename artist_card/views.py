from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .models import Song, Release, Artist
from .serializers import ArtistSerializer, ReleaseSerializer, ReleasesSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ReleaseAPIView(generics.RetrieveAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ReleasesAPIView(generics.ListCreateAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleasesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]