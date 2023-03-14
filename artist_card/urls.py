from django.urls import path
from .views import ArtistList

urlpatterns = [
    path('artists/', ArtistList.as_view()),
]
