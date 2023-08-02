from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from kariomartapi.serializers import MapSerializer
from kariomartapi.models import Map

class MapView(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            map = Map.objects.get(pk=pk)
            serializer = MapSerializer(map)
            return Response(serializer.data)
        except Map.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        maps = Map.objects.all()
        serializer = MapSerializer(maps, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        map = Map(
            name=request.data["name"],
            difficulty=request.data["difficulty"],
            theme=request.data["theme"],
            image_url=request.data["image_url"]
        )
        map.save()
        serializer = MapSerializer(map)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        try:
            map = Map.objects.get(pk=pk)
            serializer = MapSerializer(map, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Map.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            map = Map.objects.get(pk=pk)
            map.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Map.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
