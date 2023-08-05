from rest_framework import serializers
from kariomartapi.models import Cup

class CupSerializer(serializers.ModelSerializer):
    """JSON serializer for Cup model"""

    class Meta:
        model = Cup
        fields = ('id', 'name', 'race_id')
