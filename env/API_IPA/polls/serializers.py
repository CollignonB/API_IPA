from django.contrib.auth.models import User, Group
from polls.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['ulr', 'name']

class BeerSerializer(serializers.HyperlinkedModelSerializer):
    beerTypeName = serializers.CharField(source='beer_type.name')
    breweryName = serializers.CharField(source='brewery.name')
    supplierName = serializers.CharField(source='supplier.name')
    # draftFaucetNumber = serializers.IntegerField(source='draft_faucet.number')

    class Meta:
        model = Beer
        fields = ['name', 'alcool_level', 'description', 
                    'pint_price', 'half_price', 'ibu',
                     'beerTypeName', 'breweryName', 'supplierName',
                    #  'draftFaucetNumber',
                ]
        
class BeerTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BeerType
        fields = '__all__'

class BrewerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Brewery
        fields = '__all__'

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class DraftFaucetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DraftFaucet
        fields = '__all__'

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Ingredient
        fields = '__all__'

class StorageSerializer(serializers.HyperlinkedModelSerializer):
    # beerName = serializers.CharField(source= 'beer.name')
    class Meta:
        model = Storage
        fields = ['barrel_left', 'barrel_price', 
                  'working_pressure', 'working_temperature']
                  