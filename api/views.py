from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from loginUser.models import User
from myapp.models import Artist

class UserApi(APIView):

    def get(self, request):
        # Lógica para manejar la solicitud GET
        data = User.objects.filter(adminUser=0).values()
        # data = {'message': 'This is a GET request'}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        # Lógica para manejar la solicitud POST
        data = {'message': 'This is a POST request'}
        return Response(data, status=status.HTTP_201_CREATED)
    
class ArtistApi(APIView):

    def get(self, request):
        # Lógica para manejar la solicitud GET
        data = Artist.objects.values()
        # data = {'message': 'This is a GET request'}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        # Lógica para manejar la solicitud POST
        data = {'message': 'This is a POST request'}
        return Response(data, status=status.HTTP_201_CREATED)