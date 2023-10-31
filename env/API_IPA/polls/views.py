from django.shortcuts import render
from django.http import HttpResponse, Http404

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from polls.models import *
from polls.serializers import *

def index(request):
    return HttpResponse("API_IPA")

class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GrourpViewset(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# class BeerViewset(viewsets.ModelViewSet):
#     queryset = Beer.objects.all().order_by('name') 
#     serializer_class = BeerSerializer
#     permission_classes = [permissions.IsAuthenticated]
class BeerList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    List of all beers, or create new beer
    """
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    
    # def get(self, request, format = None):
    #     beers = Beer.objects.all().order_by('id')
    #     serializer = BeerSerializer(beers, many = True)
    #     return Response(serializer.data)

    # def post(Self, request, format=None):
    #     serializer = BeerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BeerDetail(mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 generics.GenericAPIView):
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a beer instance
    """
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_object(self, pk):
    #     try:
    #         return Beer.objects.get(pk=pk)
    #     except Beer.DoesNotExist:
    #         raise Http404
    
    # def get(self, request, pk, format=None):
    #     beer = self.get_object(pk)
    #     serializer = BeerSerializer(beer)
    #     return Response(serializer.data)
    

    # def put(self, request, pk, format=None):
    #     beer = self.get_object(pk)
    #     serializer = BeerSerializer(beer, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # def delete(self, request, pk, format=None):
    #     beer = self.get_object(pk)
    #     beer.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class BeerTypeList(generics.ListCreateAPIView):
    queryset = BeerType.objects.all()
    serializer_class = BeerTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class BeerTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BeerType.objects.all()
    serializer_class = BeerTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class BreweryList(generics.ListCreateAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = [permissions.IsAuthenticated]

class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]

class DraftFaucetList(generics.ListCreateAPIView):
    queryset = DraftFaucet.objects.all()
    serializer_class = DraftFaucetSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class DraftFaucetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DraftFaucet.objects.all()
    serializer_class = DraftFaucetSerializer
    permission_classes = [permissions.IsAuthenticated]

class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]

class StorageList(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class StorageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [permissions.IsAuthenticated]

# class BreweryViewset(viewsets.ModelViewSet):
#     queryset = Brewery.objects.all().order_by('name')
#     serializer_class = BrewerySerializer
#     permission_classes = [permissions.IsAuthenticated]

# class SupplierViewset(viewsets.ModelViewSet):
#     queryset = Supplier.objects.all().order_by('name')
#     serializer_class = SupplierSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class DraftFaucetViewset(viewsets.ModelViewSet):
#     queryset = DraftFaucet.objects.all()
#     serializer_class = DraftFaucetSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class IngredientViewset(viewsets.ModelViewSet):
#     queryset = Ingredient.objects.all().order_by('name')
#     serializer_class = IngredientSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class StorageViewset(viewsets.ModelViewSet):
#     queryset = Storage.objects.all()
#     serializer_class = StorageSerializer
#     permission_classes = [permissions.IsAuthenticated]
