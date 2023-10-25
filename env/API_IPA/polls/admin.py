from django.contrib import admin
from .models import *

admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(BeerType)
admin.site.register(DraftFaucet)
admin.site.register(Ingredient)
admin.site.register(Storage)
admin.site.register(Supplier)
# Register your models here.
