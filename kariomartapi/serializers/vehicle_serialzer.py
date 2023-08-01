from rest_framework import serializers
from kariomartapi.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'name', 'image_url')
