from rest_framework import serializers
from .models import Service, SoundEngineer, Arrangement, ShopCart, CartItem, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'cost', 'type']


class SoundDesignerSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)

    class Meta:
        model = SoundEngineer
        fields = ['id', 'name', 'surname', 'nickname', 'sex', 'balance', 'services']


class ArrangementSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()
    author = SoundDesignerSerializer()

    class Meta:
        model = Arrangement
        fields = ['id', 'title', 'genre', 'duration', 'cost', 'format', 'author']


class CartItemSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'quantity', 'service']


class ShopCartSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    items = CartItemSerializer(many=True)

    class Meta:
        model = ShopCart
        fields = ['id', 'artist', 'sum', 'items']
