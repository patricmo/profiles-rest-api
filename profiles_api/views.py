from django.shortcuts import render

# from django rest framwork previously installed (reqirements.txt)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

# https://www.django-rest-framework.org/api-guide/views/
# Create your views here.

class HelloApiView(APIView):
    """test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView feature"""
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditionnal Django View",
            "Gives you the mmost control over your app logic",
            "Is mapped manually to URLs",
        ]
        return Response({
            'message':'hello!',
            'an_apiview':an_apiview
        })

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ handle object update (full object)"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ handle object update (partial object) """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ handle object deletion """
        return Response({'method': 'DELETE'})

    # def __init__(self, arg):
    #     super(HelloApiView, self).__init__()
    #     self.arg = arg
