from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    """ Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get,post,patcth, put delete)',
            'is similar to a traditional Django View',
            'gives you the mosst control over you applicaiton logic',
            'is mapped manually to URLs',
        ]

        return Response({'an_apiview': an_apiview})

    def post(self,request):
        """Create a hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """handle updating an bject"""
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': ' PATCH'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """test viewwset"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'uses actions (list,create,retrieve,updte,partial_updare)'

        ]

        return Response({'a_viewset': a_viewset})

    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """henadle getting an object by its ID"""
        return Response({'hhtp_method':'GET'})

    def update(self,request,pk=None):
        """handle updating an object"""
        return Response({'http_metohd':'PUT'})

    def partial_update(self,request,pk=None):
        """handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request, pk=None):
        """handle removing an object"""
        return Response({'http_method':'DELETE'})
