from django.urls import path
from .views import UserApi, ArtistApi

urlpatterns = [
    path('api/users/', UserApi.as_view(), name='your-api-endpoint'),
    path('api/artists/', ArtistApi.as_view(), name='your-api-endpoint'),
    # Agrega otras URL para diferentes vistas de la API aquí
]