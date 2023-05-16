from django.urls import path, include
from .views import GenreList, ServiceAPIView, SoundDesignerAPIView, ArrangementAPIView, ShopCartListCreateView, \
    CartItemViewSet, cart_order_list
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart-items', CartItemViewSet)


urlpatterns = [
    path('genres/', GenreList.as_view(), name='genre_list'),
    path('services/', ServiceAPIView.as_view(), name='services'),
    path('sound_designers/', SoundDesignerAPIView.as_view(), name='sound_designers'),
    path('arrangements/', ArrangementAPIView.as_view(), name='arrangements'),

    path('carts/<int:artist_id>/', ShopCartListCreateView.as_view(), name='shopcart-list-create'),
    path('', include(router.urls)),
    path('cart_order_list/', cart_order_list, name='make_order'),
]
