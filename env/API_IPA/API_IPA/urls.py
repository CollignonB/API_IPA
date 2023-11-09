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
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GrourpViewset)
# router.register(r'beer', views.BeerViewset)
# router.register(r'beer_type', views.BeerTypeViewset)
# router.register(r'brewery', views.BreweryViewset)
# router.register(r'supplier', views.SupplierViewset)
# router.register(r'ingredient', views.IngredientViewset)
# router.register(r'draft_faucet', views.DraftFaucetViewset)
# router.register(r'storage', views.StorageViewset)
# router.register(r'beer_type', views.BeerTypeList.as_view())

user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

beer_list = views.BeerViewSet.as_view({
    'get': 'list'
})
beer_detail = views.BeerViewSet.as_view({
    'get': 'retrieve'
})
urlpatterns = [
    path('api-aut/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', views.api_root),
    path('beer/', beer_list, name='beer-list'),
    path('beer/<int:pk>/', beer_detail, name='beer-detail'),
    path('beer_type/', views.BeerTypeList.as_view(), name='beer-type-list'),
    path('beer_type/<int:pk>/', views.BeerTypeDetail.as_view(), name='beertype-detail'),
    path('brewery/', views.BreweryList.as_view(), name='brewery-list'),
    path('brewery/<int:pk>/', views.BreweryDetail.as_view(), name='brewery-detail'),
    path('supplier/', views.SupplierList.as_view(), name='supplier-list'),
    path('supplier/<int:pk>/', views.SupplierDetail.as_view(), name='supplier-detail'),
    path('draft_faucet/', views.DraftFaucetList.as_view(), name='draftfaucet-list'),
    path('draft_faucet/<int:pk>/', views.DraftFaucetDetail.as_view(), name='draftfaucet-detail'),
    path('ingredient/', views.IngredientList.as_view(), name='ingredient-list'),
    path('ingredient/<int:pk>/', views.IngredientDetail.as_view(), name='ingredient-detail'),
    path('storage/', views.StorageList.as_view()),
    path('storage/<int:pk>/', views.StorageDetail.as_view()),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name = 'user-detail'),
]