from django.db import models
from .character import Character
from .vehicle import Vehicle

class CharacterVehicle(models.Model):

    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
