from rest_framework import serializers
from kariomartapi.models import CupRace

class CupRaceSerializer(serializers.ModelSerializer):
    """JSON serializer for Cup model"""

    class Meta:
        model = CupRace
        fields = ('id', 'cup_id', 'cup_race_id')
