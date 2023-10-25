from django.db import models

# Create your models here.


class Ingredient(models.Model):

    present_in = models.ForeignKey(Beer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    origin = models.CharField(max_length=50)

class Brewery(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    origin_country = models.CharField(max_length=50)
    origin_region = models.CharField(max_length=50)

class Storage(models.Model):

    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    barrel_left = models.IntegerField()
    barrel_price = models.IntegerField()
    working_pressure = models.IntegerField()
    working_temperature = models.IntegerField()

class BeerType(models.Model):
    
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

class Supplier(models.Model):

    name = models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    
class DraftFaucet(models.Model):
    
    brand = models.CharField(max_length=200)
    co2 = models.BooleanField(default=True)
    faucet_flow = models.IntegerField()
    start_up_time = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    pressure = models.IntegerField()

class Beer(models.Model):
    # beerID = models.IntegerField(default=0)
    beer_type = models.ForeignKey(BeerType, on_delete=models.CASCADE)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    draft_faucet = models.ForeignKey(DraftFaucet, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    alcool_level = models.IntegerField()
    description = models.CharField(max_length=250)
    pint_price = models.IntegerField()
    half_price = models.IntegerField()
    ibu = models.IntegerField()
