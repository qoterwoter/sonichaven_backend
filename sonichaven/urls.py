from django.contrib import admin
from django.urls import path
from django.urls import include 
from .views import RegistrationView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('news_blog.urls')),
    path('api/', include('artist_card.urls')),
    # path('token/', views.obtain_auth_token)
    path('api-auth/', include('rest_framework.urls')),
    path('api/register/', RegistrationView.as_view()),
    path('api/login/', LoginView.as_view()),

]
