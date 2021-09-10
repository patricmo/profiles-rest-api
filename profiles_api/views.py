from django.shortcuts import render

# from django rest framwork previously installed (reqirements.txt)
from rest_framework.views import APIView
from rest_framework.response import Response

# https://www.django-rest-framework.org/api-guide/views/
# Create your views here.

class HelloApiView(APIView):
    """test API View"""

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

    # def __init__(self, arg):
    #     super(HelloApiView, self).__init__()
    #     self.arg = arg
