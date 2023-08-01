from django.db import models

class Map(models.Model):

    name = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
