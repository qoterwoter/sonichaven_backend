from django.urls import path
from .views import NewsList

urlpatterns = [
    path('news/', NewsList.as_view()),
    # path('news/<int:pk>/', NewsDetail.as_view()),
    # path('news-article/<int:pk>/', NewsArticleDetail.as_view()),
]
