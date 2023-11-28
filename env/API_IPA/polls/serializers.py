from django.contrib.auth.models import User, Group
from rest_framework.fields import empty
from polls.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['ulr', 'name']

class DynamicFieldsCategorySerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class BreweryBeerListSerializer(DynamicFieldsCategorySerializer):
    class Meta:
        model = Beer
        fields = ['id', 'name']


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

class BeerTypeSerializer(DynamicFieldsCategorySerializer):

    class Meta:
        model = BeerType
        fields = '__all__'


class SupplierSerializer(DynamicFieldsCategorySerializer):

    class Meta:
        model = Supplier
        fields = '__all__'

class DraftFaucetSerializer(DynamicFieldsCategorySerializer):

    class Meta:
        model = DraftFaucet
        fields = '__all__'

class IngredientSerializer(DynamicFieldsCategorySerializer):

    class Meta :
        model = Ingredient
        fields = '__all__'

class StorageSerializer(DynamicFieldsCategorySerializer):
    class Meta:
        model = Storage
        fields = ['barrel_left', 'barrel_price', 
                  'working_pressure', 'working_temperature']
                  


class BrewerySerializer(DynamicFieldsCategorySerializer):

    # beer_produced = BeerSerializer(fields = ['id', 'name'], many= True, allow_null=True)
    # beer_produced = serializers.CharField(source='models.Beer.id')
    # beer = BeerSerializer(many=True, fields=['id', 'name'])

    class Meta :
        model = Brewery
        fields = ['id', 'name', 'url', 'description',
                  'origin_country', 'origin_region']
        # fields = '__all__'
    
    def to_internal_value(self, data):
        resource_data = data['beer_id', 'beer_name']

        return super().to_internal_value(resource_data)

class BeerSerializer(DynamicFieldsCategorySerializer):

    brewery = BrewerySerializer(fields = ('name', 'url'))
    beer_type = BeerTypeSerializer(fields = ('name', 'url'))
    supplier = SupplierSerializer(fields = ('name', 'url'))
    # ingredient = IngredientSerializer(fields = ('name'))
    class Meta:
        model = Beer
        fields = ['id', 'url', 'name','alcool_level', 'description', 'pint_price', 'half_price','ibu', 'brewery', 'beer_type', 'supplier', 'draft_faucet']
        # fields = '__all__'