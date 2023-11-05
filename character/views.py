from django.shortcuts import render

from .serializers import CharacterSerializer
from .models import Character
from rest_framework import generics

# Character 정보 저장하기
class CharacterCreate(generics.CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

# Character 정보 불러오기
class CharacterList(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

