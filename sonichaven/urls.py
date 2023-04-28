from django.contrib import admin
from django.urls import path
from django.urls import include 
from .views import RegistrationView, LoginView
import corsheaders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('news_blog.urls')),
    path('api/', include('artist_card.urls')),
    path('api/', include('staff_service.urls')),
    path('api/register/', RegistrationView.as_view()),
    path('api/login/', LoginView.as_view()),
]

urlpatterns += [path('api/', include('corsheaders.urls'))]
