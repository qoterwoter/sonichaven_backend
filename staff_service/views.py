from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, pagination, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Service, SoundEngineer, Arrangement, ShopCart, CartItem, Genre
from artist_card.models import Artist
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
    queryset = SoundEngineer.objects.all()
    serializer_class = SoundDesignerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ArrangementAPIView(generics.ListCreateAPIView):
    queryset = Arrangement.objects.all()
    serializer_class = ArrangementSerializer

class ShopCartListCreateView(generics.ListCreateAPIView):
    queryset = ShopCart.objects.all()
    serializer_class = ShopCartSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user.artist)

    def get_queryset(self):
        artist = Artist.objects.filter(user=self.request.user).first()
        return ShopCart.objects.filter(artist=artist)

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class CartItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.cart.artist != self.request.user.artist:
            self.permission_denied(self.request)
        return obj