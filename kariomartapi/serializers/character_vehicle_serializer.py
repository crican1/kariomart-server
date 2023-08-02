from rest_framework import serializers
from kariomartapi.models import CharacterVehicle

class CharacterVehicleSerializer(serializers.ModelSerializer):
    """JSON serializer for CharacterVehicle model"""

    class Meta:
        model = CharacterVehicle
        fields = ('id', 'character_id', 'vehicle_id')
