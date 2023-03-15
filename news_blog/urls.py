from django.urls import path
from .views import NewsList

urlpatterns = [
    path('news/', NewsList.as_view(), name='All news'),
    path('news_detail/<int:id>/', NewsList.as_view(), name='News Detail'),
]
