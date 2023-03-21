from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, pagination, viewsets, generics

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Service, SoundDesigner, Arrangement, ShopCart, CartItem, Genre
from .serializers import ServiceSerializer, SoundDesignerSerializer, ArrangementSerializer, ShopCartSerializer, CartItemSerializer, GenreSerializer

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

class ServiceAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SoundDesignerAPIView(generics.ListCreateAPIView):
    queryset = SoundDesigner.objects.all()
    serializer_class = SoundDesignerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ArrangementAPIView(generics.ListCreateAPIView):
    queryset = Arrangement.objects.all()
    serializer_class = ArrangementSerializer

class ShopCartListCreateView(generics.ListCreateAPIView):
    queryset = ShopCart.objects.all()
    serializer_class = ShopCartSerializer

class ShopCartByArtist(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, artist_id):
        carts = ShopCart.objects.filter(artist=artist_id)
        serializer = ShopCartSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)