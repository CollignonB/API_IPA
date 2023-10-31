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
"""

ancienne version de BeerSerializer

# class BeerSerializer(serializers.HyperlinkedModelSerializer):
#     # beerTypeName = serializers.CharField(source='beer_type.name')
#     # breweryName = serializers.CharField(source='brewery.name')
#     # supplierName = serializers.CharField(source='supplier.name')
#     id = serializers.IntegerField(read_only=True)
#     url = serializers.CharField(read_only=True)
#     # draftFaucetNumber = serializers.IntegerField(source='draft_faucet.number')

#     class Meta:
#         model = Beer
#         # fields = ['id', 'url', 'name', 'alcool_level', 'description', 
#         #             'pint_price', 'half_price', 'ibu',
#         #              'beerTypeName', 'breweryName', 'supplierName',
#         #             #  'draftFaucetNumber',
#         #         ]
#         fields = '__all__'

# class BeerSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required = True, allow_blank = False, max_length = 60)
#     alcool_level = serializers.IntegerField()
#     description = serializers.CharField(max_length = 250)
#     pint_price = serializers.IntegerField()
#     half_price = serializers.IntegerField()
#     ibu = serializers.IntegerField()
#     beer_type = serializers.CharField()
#     brewery = serializers.CharField()
#     draft_faucet = serializers.CharField()
#     supplier = serializers.CharField()

#     def create(self, validated_data):
#         return Beer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.alcool_level = validated_data.get('alccol_level', instance.alcool_level)
#         instance.description = validated_data.get('description', instance.description)
#         instance.pint_price = validated_data.get('pint_price', instance.pint_price)
#         instance.half_price = validated_data.get('half_price', instance.half_price)
#         instance.ibu = validated_data.get('ibu', instance.ibu)
#         instance.beer_type = validated_data.get('beer_type', instance.beer_type)
#         instance.brewery = validated_data.get('brewery', instance.brewery)
#         instance.draft_faucet = validated_data.get('draft_faucet', instance.draft_faucet)
#         instance.supplier = validated_data.get('supplier', instance.supplier)
#         instance.save()
#         return instance
"""
class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = '__all__'

class BeerTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BeerType
        fields = '__all__'

class BrewerySerializer(serializers.ModelSerializer):
    class Meta :
        model = Brewery
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class DraftFaucetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DraftFaucet
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta :
        model = Ingredient
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['barrel_left', 'barrel_price', 
                  'working_pressure', 'working_temperature']
                  