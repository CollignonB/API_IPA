"""
URL configuration for API_IPA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from polls import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GrourpViewset)
router.register(r'beer', views.BeerViewset)
router.register(r'beer_type', views.BeerTypeViewset)
router.register(r'brewery', views.BreweryViewset)
router.register(r'supplier', views.SupplierViewset)
router.register(r'ingredient', views.IngredientViewset)
router.register(r'draft_faucet', views.DraftFaucetViewset)
router.register(r'storage', views.StorageViewset)


urlpatterns = [
    path('polls/', include("polls.urls")),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('api-aut/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api_beer/', include('rest_framework.urls', namespace='beer'))
]
