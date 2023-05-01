from rest_framework import serializers
from .models import Service, SoundEngineer, Arrangement, ShopCart, CartItem, Genre, Order, OrderItem


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'cost', 'type', 'description']


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


class CartItemUpdateSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'quantity', 'service']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, data):
        cart = data['cart']
        service = data['service']

        # Check if the combination of cart and service already exists
        queryset = CartItem.objects.filter(cart=cart, service=service)

        if self.instance:
            # Exclude the current object being updated from the queryset
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError('CartItem already exists')

        return data

    def update(self, instance, validated_data):
        # Check if the combination of cart and service already exists for other instances
        cart = validated_data.get('cart', instance.cart)
        service = validated_data.get('service', instance.service)
        if CartItem.objects.filter(cart=cart, service=service).exclude(pk=instance.pk).exists():
            raise serializers.ValidationError('CartItem already exists')
        return super().update(instance, validated_data)


class ShopCartSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    items = CartItemUpdateSerializer(many=True)

    class Meta:
        model = ShopCart
        fields = ['id', 'artist', 'sum', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        shop_cart = ShopCart.objects.create(**validated_data)
        for item_data in items_data:
            CartItem.objects.create(cart=shop_cart, **item_data)
        return shop_cart


class OrderItemSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = OrderItem
        fields = ['id','service','quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'sum', 'status', 'items']
