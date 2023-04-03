from django.urls import path
from .views import ArtistList, ReleaseAPIView, ReleasesAPIView, artist_info

urlpatterns = [
    path('artists/', ArtistList.as_view()),
    path('artist-info/', artist_info, name='artist-info'),
    path('releases/', ReleasesAPIView.as_view(), name='albums_list'),
    path('release/<int:artist_id>/', ReleaseAPIView.as_view(), name='album_detail'),
]
