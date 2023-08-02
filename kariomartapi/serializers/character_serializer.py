from rest_framework import serializers
from kariomartapi.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    """JSON serializer for characters"""

    class Meta:
        model = Character
        fields = ('id', 'name', 'favorite', 'image_url')
