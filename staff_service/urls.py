from django.urls import path
from .views import GenreList, ServiceAPIView, SoundDesignerAPIView, ArrangementAPIView, ShopCartListCreateView, ShopCartByArtist

urlpatterns = [
    path('genres/', GenreList.as_view(), name='genre_list'),
    path('services/', ServiceAPIView.as_view(), name='services'),
    path('sound_designers/', SoundDesignerAPIView.as_view(), name='sound_designers'),
    path('arrangements/', ArrangementAPIView.as_view(), name='arrangements'),
    path('carts/', ShopCartListCreateView.as_view(), name='shopcart-list-create'),
    path('carts/<int:artist_id>/', ShopCartByArtist.as_view(), name='shopcart-retrieve-update-destroy'),
]
