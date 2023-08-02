from rest_framework import serializers
from kariomartapi.models import Map

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'name', 'difficulty', 'theme', 'image_url')
