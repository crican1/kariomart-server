from kariomartapi.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = User
        fields = ('id', 
                  'uid', 
                  'name',
                 )
        depth = 2
