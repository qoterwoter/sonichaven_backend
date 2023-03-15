from rest_framework import generics
from .models import News, NewsArticle
from .serializers import NewsSerializer, NewsArticleSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

class NewsPagination(PageNumberPagination):
    page_size = 10

class NewsList(APIView):
    def get(self, request):
        news = News.objects.all().order_by('-created_at')
        paginator = NewsPagination()
        result_page = paginator.paginate_queryset(news, request)
        serializer = NewsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

