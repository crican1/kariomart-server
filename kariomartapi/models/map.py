from django.db import models

class Map(models.Model):

    name = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    image_url = models.CharField(max_length=1000, default=1)
