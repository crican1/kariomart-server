from django.db import models
from .map import Map
from .character_vehicle import CharacterVehicle

class Race(models.Model):

    character_vehicle_id = models.ForeignKey(CharacterVehicle, on_delete=models.CASCADE)
    
    map_id = models.ForeignKey(Map, on_delete=models.CASCADE)
