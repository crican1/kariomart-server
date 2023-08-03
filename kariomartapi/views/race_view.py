from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from kariomartapi.serializers import RaceSerializer
from kariomartapi. models import CharacterVehicle, Map, Race

class RaceView(ViewSet):
  
    def retrieve(self, request, pk=None):
        try:
            race = Race.objects.get(pk=pk)
            serializer = RaceSerializer(race)
            return Response(serializer.data)
        except Race.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        race = Race.objects.all()
        id = request.query_params.get('race', None)

        if id is not None:
            race = Race.filter(user_id=id)
        
        serializer = RaceSerializer(race, many=True)
        return Response(serializer.data)

    def create(self, request):

        character_vehicle_id = CharacterVehicle.objects.get(pk=request.data["character_vehicle_id"])

        map_id = Map.objects.get(pk=request.data["map_id"])
        
        race = Race.objects.create(
            character_vehicle_id=character_vehicle_id,
            map_id=map_id
        )
        
        serializer = RaceSerializer(race)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a product

        Returns:
        Response -- Empty body with 204 status code
        """

        race = Race.objects.get(pk=pk)
        race.character_vehicle_id = request.data["character_vehicle_id"]
        race.map_id = request.data["map_id"]

        race.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Delete Product
        """
        race = Race.objects.get(pk=pk)
        race.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
