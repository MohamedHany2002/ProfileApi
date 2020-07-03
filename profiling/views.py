from django.shortcuts import render
from .serializers import profile,profileSerializer,itemSerializer
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .permissions import profileViewPermission,itemPermission
from rest_framework import viewsets,filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .models import feedItem
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated


# Create your views here.


class get_profile(APIView):
    serializer_class = profile
    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self,request):
        serializer = profile(data=request.data)
        if serializer.is_valid():
            name=serializer.data['name']
            return Response({'name':name})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class hellViewset(viewsets.ViewSet):
    def list(self,request):
        a_viewset=['sdf','sdf','sdf']
        return Response({'viewset':a_viewset})

    def create(self,request):
        serializer_class = profile
        serializing=profile(data=request.data)
        if serializing.is_valid():
            name = serializing.data['name']
            return Response({'data':name})
        else:
            return Response(serializing.errors,status=status.HTTP_400_BAD_REQUEST)



class profileViewSet(viewsets.ModelViewSet):
    serializer_class=profileSerializer
    queryset= User.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(profileViewPermission,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('username','email',)

class LoginViewSet(viewsets.ViewSet):
    serializer_class=AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken().post(request)


class itemViewSet(viewsets.ModelViewSet):
    serializer_class = itemSerializer
    queryset=feedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes=(IsAuthenticated,itemPermission,)


    def perform_create(self,serializer):
        serializer.save(user=self.request.user)





    # def list(self,request):
    #     pass

    # def create(self,request):
    #     serializer=profileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'data':serializer.data})
    #     else:
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




