from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from kariomartapi.serializers import CharacterSerializer
from kariomartapi.models import Character 

class CharacterView(ViewSet):
    
    def retrieve(self, request, pk=None):
      
        character = Character.objects.get(pk=pk)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
    
    def list(self, request):
        characters = Character.objects.all()
        id = request.query_params.get('character', None)
        print('products for id:', id)
        if id is not None:
            characters = characters.filter(user_id=id)
        
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        character = Character(
            name=request.data["name"],
            favorite=request.data["favorite"],
            image_url=request.data["image_url"]
        )
        character.save()
        serializer = CharacterSerializer(character)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def update(self, request, pk=None):
        character = Character.objects.get(pk=pk)
        serializer = CharacterSerializer(character, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        try:
            character = Character.objects.get(pk=pk)
            character.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Character.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
