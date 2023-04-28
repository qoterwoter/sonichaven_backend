from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, pagination, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Service, SoundEngineer, Arrangement, ShopCart, CartItem, Genre, Order
from artist_card.models import Artist
from .serializers import ServiceSerializer, SoundDesignerSerializer, ArrangementSerializer, ShopCartSerializer, \
    CartItemSerializer, GenreSerializer, OrderSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes


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

    def options(self, request, *args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response['Access-Control-Allow-Headers'] = 'Authorization'
        return response


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

        # Call calculate_cart_sum on the cart instance after the update
        cart = instance.cart
        cart.calculate_cart_sum()

        return Response(serializer.data)

    def perform_destroy(self, instance):
        cart = instance.cart
        super().perform_destroy(instance)

        # Call calculate_cart_sum on the cart instance after the delete
        cart.calculate_cart_sum()

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def cart_order_list(request):
    if request.method == 'GET':
        # Retrieve the current cart for the authenticated user
        artist = request.user.artist_set.first()
        current_cart = ShopCart.objects.filter(artist=artist).first()

        # If there is no current cart, return an empty response
        if not current_cart:
            return Response({'message': 'No current cart'}, status=status.HTTP_204_NO_CONTENT)

        # Retrieve the orders for the current cart
        orders = current_cart.orders.all()

        # Serialize the orders and return the response
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Retrieve the current cart for the authenticated user
        artist = request.user.artist_set.first()
        cart = artist.carts.first()

        # Create a new order for the cart and add the cart's items to the order
        order = Order.objects.create(cart=cart)
        order.items.set(cart.items.all())

        # Remove the items from the cart and recalculate the cart's sum
        cart.items.set([])
        cart.calculate_cart_sum()

        # Return the response
        return Response({'status': 'ok', 'message': 'Order created'})