from django.db import models

class Vehicle(models.Model):

    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=1000, default=1)
