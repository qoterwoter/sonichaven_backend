from django.urls import path
from .views import NewsList, NewsDetail

urlpatterns = [
    path('news/', NewsList.as_view(), name='All_news'),
    path('news_detail/<int:pk>/', NewsDetail.as_view(), name='News_Detail'),
]
