from django.urls import path
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .views import GenreList

urlpatterns = [
    path('genres/', GenreList.as_view(), name='genre_list'),
]
