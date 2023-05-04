from django.urls import path, include
from .views import SongViewSet, ArtistList, ReleaseListByArtist, ReleaseViewSet, artist_info, ArtistDetail
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'releases', ReleaseViewSet)

urlpatterns = [
    path('artists/', ArtistList.as_view()),
    path('artists/<int:pk>/', ArtistDetail.as_view(), name='artist-detail'),
    path('artist-info/', artist_info, name='artist-info'),
    path('', include(router.urls)),
    path('release/<int:artist_id>/', ReleaseListByArtist.as_view(), name='album_detail'),
    path('songs/', SongViewSet.as_view({'get': 'list', 'post': 'create'}), name='song-list'),
    path('song/<int:pk>/', SongViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='song-detail'),
]
