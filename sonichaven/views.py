from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from artist_card.models import Artist
from artist_card.serializers import ArtistSerializer
from staff_service.models import ShopCart
from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            artist = get_object_or_404(Artist, user=user)
            artist_data = ArtistSerializer(artist).data
            user_data = UserSerializer(user).data
            user_data['artist'] = artist_data

            cart = ShopCart.objects.filter(artist=artist).first()
            user_data['cart_id'] = cart.id if cart else None
            token, created = Token.objects.get_or_create(user=user)
            user_data['token'] = token.key
            return Response(user_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        # Retrieve related artist info
        artist = get_object_or_404(Artist, user=user)
        artist_data = ArtistSerializer(artist).data

        # Serialize and return user data with related artist info
        user_data = UserSerializer(user).data
        user_data['artist'] = artist_data
        user_data['token'] = token.key

        # Retrieve cart ID
        cart = ShopCart.objects.filter(artist=artist).first()
        user_data['cart_id'] = cart.id if cart else None

        return Response(user_data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if 'profile_image' in serializer.validated_data:
            serializer.instance.profile_image = serializer.validated_data['profile_image']
        if 'username' in serializer.validated_data:
            serializer.instance.username = serializer.validated_data['username']
        if 'password' in serializer.validated_data:
            serializer.instance.password = make_password(serializer.validated_data['password'])
        serializer.save()
        updated_user = serializer.instance
        updated_user_data = UserSerializer(updated_user).data
        return Response(updated_user_data, status=status.HTTP_200_OK)
    def perform_destroy(self, instance):
        instance.delete()

    def update(self, request, *args, **kwargs):
        # check if user is updating their own profile
        if request.user.id != int(kwargs['pk']):
            return Response({'error': 'Not authorized to update this user.'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)
