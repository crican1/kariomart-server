from django.db import models
from .map import Map
from .character import Character
from .vehicle import Vehicle

class Race(models.Model):

    character_id = models.ForeignKey(Character, on_delete=models.CASCADE, default=1)
    
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=1)
    
    map_id = models.ForeignKey(Map, on_delete=models.CASCADE)
    
    uid = models.CharField(max_length=50, default=1)
