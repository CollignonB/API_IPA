from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
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

class BeerViewset(viewsets.ModelViewSet):
    queryset = Beer.objects.all().order_by('name')
    serializer_class = BeerSerializer
    permission_classes = [permissions.IsAuthenticated]

class BeerTypeViewset(viewsets.ModelViewSet):
    queryset = BeerType.objects.all().order_by('name')
    serializer_class = BeerTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class BreweryViewset(viewsets.ModelViewSet):
    queryset = Brewery.objects.all().order_by('name')
    serializer_class = BrewerySerializer
    permission_classes = [permissions.IsAuthenticated]

class SupplierViewset(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]

class DraftFaucetViewset(viewsets.ModelViewSet):
    queryset = DraftFaucet.objects.all()
    serializer_class = DraftFaucetSerializer
    permission_classes = [permissions.IsAuthenticated]

class IngredientViewset(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]

class StorageViewset(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [permissions.IsAuthenticated]
