from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from kariomartapi.views import CharacterView, VehicleView, MapView, CharacterVehicleView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'characters', CharacterView, 'character')
router.register(r'vehicles', VehicleView, 'vehicle')
router.register(r'maps', MapView, 'map')
router.register(r'character_vehicles', CharacterVehicleView, 'character_vehicle')

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(router.urls)),
]
