from rest_framework import serializers
from kariomartapi.models import Race


class  RaceSerializer(serializers.ModelSerializer):
    """JSON serializer for productss
    """
    class Meta:
        model = Race
        fields = ('id', 'map_id', 'character_id', 'vehicle_id', 'uid')
        depth = 3
