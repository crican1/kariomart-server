from django.db import models

class Character(models.Model):

    name = models.CharField(max_length=50)
    favorite = models.BooleanField(null=True, blank=True)
    image_url = models.CharField(max_length=1000, default=1)
