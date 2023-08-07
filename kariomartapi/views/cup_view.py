from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from kariomartapi.models import Cup, Race
from kariomartapi.serializers import CupSerializer

class CupView(ViewSet):
  
    """Kariomart cup view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single cup
        Returns:
            Response -- JSON serialized cup
        """
        try:
            cup = Cup.objects.get(pk=pk)
            serializer = CupSerializer(cup)
            return Response(serializer.data)
        except Cup.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all cups

        Returns:
            Response -- JSON serialized list of cups
        """
                
        cup = Cup.objects.all()
        serializer = CupSerializer(cup, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized Cup instance
        """
        race_id = Race.objects.get(pk=request.data["raceId"])
        
        cup = Cup.objects.create(
            name=request.data["name"],
            race_id=race_id,
        )
        serializer = CupSerializer(cup)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Retrieve the existing Cup instance based on the given pk (primary key)
        try:
            cup = Cup.objects.get(pk=pk)
        except Cup.DoesNotExist:
            return Response({"error": "Cup not found"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the Race instance based on race_id from the request data
        race_id = request.data.get("race_id")
        try:
            race = Race.objects.get(pk=race_id)
        except Race.DoesNotExist:
            return Response({"error": "Race not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update the Cup instance with the retrieved Race instances
        cup.name = request.data["name"]
        cup.race_id = race
        Cup.save()

        serializer = CupSerializer(cup)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Delete Cup
        """
        cup = Cup.objects.get(pk=pk)
        cup.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
