from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from kariomartapi.serializers.vehicle_serialzer import VehicleSerializer
from kariomartapi.models import Vehicle

class VehicleView(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            vehicle = Vehicle.objects.get(pk=pk)
            serializer = VehicleSerializer(vehicle)
            return Response(serializer.data)
        except Vehicle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def create(self, request):
        vehicle = Vehicle(
            name=request.data["name"],
            image_url=request.data["image_url"]
        )
        vehicle.save()
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            vehicle = Vehicle.objects.get(pk=pk)
            serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Vehicle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            vehicle = Vehicle.objects.get(pk=pk)
            vehicle.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vehicle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
