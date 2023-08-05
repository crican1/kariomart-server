from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from kariomartapi.views import CharacterView, VehicleView, MapView, RaceView, UserView
from kariomartapi.views.auth import register_user, check_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'characters', CharacterView, 'character')
router.register(r'vehicles', VehicleView, 'vehicle')
router.register(r'maps', MapView, 'map')
router.register(r'races', RaceView, 'race')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(router.urls)),
     path('register', register_user),
    path('checkuser', check_user),
]
