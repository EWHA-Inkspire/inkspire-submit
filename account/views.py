from django.shortcuts import render

from .serializers import UserSerializer, CharacterSerializer
from .models import User, Character
from rest_framework import generics

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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