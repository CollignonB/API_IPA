from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.models import User, Group
from django.db import connection

from rest_framework import viewsets, permissions, status, mixins, generics, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from polls.models import *
from polls.serializers import *
from polls.permissions import IsOwnerOrReadOnly

def index(request):
    return HttpResponse("API_IPA")

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'beer': reverse('beer-list', request=request, format=format),
        'beer-type': reverse('beer-type-list', request=request, format=format),
        'brewery': reverse('brewery-list', request=request, format=format),
        'ingredient': reverse('ingredient-list', request=request, format=format),
        'supplier': reverse('supplier-list', request=request, format=format),
        'draft faucet' : reverse('draftfaucet-list', request=request, format=format)
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class BeerViewSet(viewsets.ModelViewSet):

    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

# class BeerList(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                generics.GenericAPIView):

#     queryset = Beer.objects.all()
#     serializer_class = BeerSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)    

# class BeerDetail(generics.RetrieveUpdateDestroyAPIView):

    # queryset = Beer.objects.all()
    # serializer_class = BeerSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BeerTypeList(generics.ListCreateAPIView):
    queryset = BeerType.objects.all()
    serializer_class = BeerTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BeerTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BeerType.objects.all()
    serializer_class = BeerTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BreweryList(generics.ListCreateAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
 
class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DraftFaucetList(generics.ListCreateAPIView):
    queryset = DraftFaucet.objects.all()
    serializer_class = DraftFaucetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class DraftFaucetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DraftFaucet.objects.all()
    serializer_class = DraftFaucetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StorageList(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class StorageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class BreweryViewset(viewsets.ModelViewSet):
#     queryset = Brewery.objects.all()
#     serializer_class = BrewerySerializer
#     permission_classes = [permissions.IsAuthenticated]

# class SupplierViewset(viewsets.ModelViewSet):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class DraftFaucetViewset(viewsets.ModelViewSet):
#     queryset = DraftFaucet.objects.all()
#     serializer_class = DraftFaucetSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class IngredientViewset(viewsets.ModelViewSet):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class StorageViewset(viewsets.ModelViewSet):
#     queryset = Storage.objects.all()
#     serializer_class = StorageSerializer
#     permission_classes = [permissions.IsAuthenticated]
