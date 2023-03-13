from django.urls import path
from artist_card.views import ArtistTokenObtainPairView

urlpatterns = [
    path('api/token/', ArtistTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
