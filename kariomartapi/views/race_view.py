from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from kariomartapi.serializers import RaceSerializer
from kariomartapi. models import Map, Race, Character, Vehicle

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
        character_id = request.data.get("character_id")
        vehicle_id = request.data.get("vehicle_id")
        map_id = request.data.get("map_id")
        uid = request.data.get("uid")

        try:
            character = Character.objects.get(pk=character_id)
            vehicle = Vehicle.objects.get(pk=vehicle_id)
            map_instance = Map.objects.get(pk=map_id)

            race = Race(
                character_id=character,
                vehicle_id=vehicle,
                map_id=map_instance,
                uid=uid
            )
            race.save()

            serializer = RaceSerializer(race)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (Character.DoesNotExist, Vehicle.DoesNotExist, Map.DoesNotExist) as e:
            return Response({"error": "Invalid character, vehicle, or map ID."}, status=status.HTTP_400_BAD_REQUEST)

    
    def update(self, request, pk=None):
        """Handle PUT requests for a race

        Returns:
        Response -- Empty body with 204 status code
        """
        try:
            race = Race.objects.get(pk=pk)

            # Get the updated map_id from the request data or keep the existing value if not provided
            map_id = request.data.get("map_id", race.map_id_id)

            # Ensure that the map_id is a valid Map instance
            try:
                map_instance = Map.objects.get(pk=map_id)
            except Map.DoesNotExist:
                return Response({"error": "Invalid map ID."}, status=status.HTTP_400_BAD_REQUEST)

            # Update the race object with the new map_id
            race.map_id_id = map_instance

            race.save()

            return Response({'message': 'Race Updated'}, status=status.HTTP_204_NO_CONTENT)
        except Race.DoesNotExist:
            return Response({"error": "Invalid race ID."}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        """Delete Product
        """
        race = Race.objects.get(pk=pk)
        race.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
