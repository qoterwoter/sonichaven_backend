from rest_framework import generics, viewsets
from .models import News, NewsArticle
from .serializers import NewsSerializer, NewsDetailSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

class NewsPagination(PageNumberPagination):
    page_size = 5 # specify the number of news items per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class NewsList(APIView):
    def get(self, request):
        news = News.objects.all().order_by('-created_at')
        paginator = NewsPagination()   
        result_page = paginator.paginate_queryset(news, request)
        serializer = NewsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer