from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from kariomartapi.serializers import CharacterVehicleSerializer
from kariomartapi. models import CharacterVehicle, Character, Vehicle

class CharacterVehicleView(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            character_vehicle = CharacterVehicle.objects.get(pk=pk)
            serializer = CharacterVehicleSerializer(character_vehicle)
            return Response(serializer.data)
        except CharacterVehicle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        character_vehicles = CharacterVehicle.objects.all()
        serializer = CharacterVehicleSerializer(character_vehicles, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Retrieve the Character instance based on character_id
        character_id = request.data.get("character_id")
        try:
            character = Character.objects.get(pk=character_id)
        except Character.DoesNotExist:
            return Response({"error": "Character not found"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the Vehicle instance based on vehicle_id
        vehicle_id = request.data.get("vehicle_id")
        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            return Response({"error": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create the CharacterVehicle instance with the retrieved Character and Vehicle instances
        character_vehicle = CharacterVehicle(
            character_id=character,
            vehicle_id=vehicle
        )
        character_vehicle.save()

        serializer = CharacterVehicleSerializer(character_vehicle)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        # Retrieve the existing CharacterVehicle instance based on the given pk (primary key)
        try:
            character_vehicle = CharacterVehicle.objects.get(pk=pk)
        except CharacterVehicle.DoesNotExist:
            return Response({"error": "CharacterVehicle not found"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the Character instance based on character_id from the request data
        character_id = request.data.get("character_id")
        try:
            character = Character.objects.get(pk=character_id)
        except Character.DoesNotExist:
            return Response({"error": "Character not found"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the Vehicle instance based on vehicle_id from the request data
        vehicle_id = request.data.get("vehicle_id")
        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            return Response({"error": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update the CharacterVehicle instance with the retrieved Character and Vehicle instances
        character_vehicle.character_id = character
        character_vehicle.vehicle_id = vehicle
        character_vehicle.save()

        serializer = CharacterVehicleSerializer(character_vehicle)
        return Response(serializer.data)
 
    def destroy(self, request, pk=None):
        # Retrieve the existing CharacterVehicle instance based on the given pk (primary key)
        try:
            character_vehicle = CharacterVehicle.objects.get(pk=pk)
        except CharacterVehicle.DoesNotExist:
            return Response({"error": "CharacterVehicle not found"}, status=status.HTTP_404_NOT_FOUND)

        # Delete the CharacterVehicle instance
        character_vehicle.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
