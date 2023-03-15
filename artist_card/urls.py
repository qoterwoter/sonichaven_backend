from django.urls import path
from .views import ArtistList, ReleaseAPIView, ReleasesAPIView

urlpatterns = [
    path('artists/', ArtistList.as_view()),
    path('releases/', ReleasesAPIView.as_view(), name='albums_list'),
    path('release/<int:pk>/', ReleaseAPIView.as_view(), name='album_detail'),
]
