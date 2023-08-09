from django.db import models
from .race import Race

class Cup(models.Model):

    name = models.CharField(max_length=50)
    race_id = models.ForeignKey(Race, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=1000, default=1)
