from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, pagination

from .models import Genre
from .serializers import GenreSerializer

class GenrePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        paginator = GenrePagination()   
        result_page = paginator.paginate_queryset(genres, request)
        serializer = GenreSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
