from rest_framework import serializers
from kariomartapi.models import Race


class  RaceSerializer(serializers.ModelSerializer):
    """JSON serializer for productss
    """
    class Meta:
        model = Race
        fields = ('id', 'character_vehicle_id', 'map_id')
        depth = 3
