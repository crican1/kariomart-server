from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from kariomartapi.models import Cup, Race, CupRace
from kariomartapi.serializers import CupRaceSerializer

class CupRaceView(ViewSet):
  
    """Kariomart cup_race view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single cup_race
        Returns:
            Response -- JSON serialized cup_race
        """
        try:
            cup_race = CupRace.objects.get(pk=pk)
            serializer = CupRaceSerializer(cup_race)
            return Response(serializer.data)
        except Cup.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all cup_races

        Returns:
            Response -- JSON serialized list of cup_races
        """
                
        cup_race = CupRace.objects.all()
        serializer = CupRaceSerializer(cup_race, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized CupRace instance
        """
        cup_id = Cup.objects.get(pk=request.data["cupId"])
        cup_race_id = Race.objects.get(pk=request.data["cupRaceId"])
        
        cup_race = CupRace.objects.create(
            cup_id=cup_id,
            cup_race_id=cup_race_id,
        )
        serializer = CupRaceSerializer(cup_race)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Retrieve the existing Cup instance based on the given pk (primary key)
        try:
            cup_race = CupRace.objects.get(pk=pk)
        except Cup.DoesNotExist:
            return Response({"error": "Cup not found"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the Race instance based on race_id from the request data
        cup_id = request.data.get("cup_id")
        try:
            cup_race = CupRace.objects.get(pk=cup_id)
        except Race.DoesNotExist:
            return Response({"error": "Cup not found"}, status=status.HTTP_404_NOT_FOUND)

        cup_race_id = request.data.get("cup_race_id")
        try:
            cup_race = CupRace.objects.get(pk="cup_race_id")
        except Race.DoesNotExist:
            return Response({"error": "Race not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update the Cup instance with the retrieved Race instances
        cup_race.cup_id = cup_id
        cup_race.cup_race_id = cup_race_id
        Cup.save()

        serializer = CupRaceSerializer(cup_race)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Delete Cup
        """
        cup_race = CupRace.objects.get(pk=pk)
        cup_race.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
