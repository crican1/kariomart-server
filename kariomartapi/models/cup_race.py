from django.db import models
from .cup import Cup
from .race import Race

class CupRace(models.Model):

    cup_id = models.ForeignKey(Cup, on_delete=models.CASCADE)
    cup_race_id = models.ForeignKey(Race, on_delete=models.CASCADE)
