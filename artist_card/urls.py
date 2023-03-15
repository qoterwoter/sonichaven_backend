from django.urls import path
from .views import ArtistList, AlbumAPIView, AlbumsAPIView

urlpatterns = [
    path('artists/', ArtistList.as_view()),
    path('albums/', AlbumsAPIView.as_view(), name='albums_list'),
    path('album/<int:pk>/', AlbumAPIView.as_view(), name='album_detail'),
]
