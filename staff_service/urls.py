from django.urls import path
from .views import GenreList, ServiceAPIView, SoundDesignerAPIView

urlpatterns = [
    path('genres/', GenreList.as_view(), name='genre_list'),
    path('services/', ServiceAPIView.as_view(), name='services'),
    path('sounddesigners/', SoundDesignerAPIView.as_view(), name='services'),
]
