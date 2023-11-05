from .models import User, Character
from rest_framework import serializers

# 회원 Serializer
class UserSerializer(serializers.ModelSerializer):
    # create 함수 overriding -> validated_data (유효성 검증 통과한 값) 기반 User 객체 생성
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            nickname = validated_data['nickname']
        )
        return user
    
    class Meta:
        model = User
        fields = ['nickname', 'email', 'password']

# 캐릭터 Serializer
class CharacterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        character = Character.objects.create(
            user_id = validated_data['user_id'],
            name = validated_data['name']
        )
        return character
    
    # JSON 형식으로 serialize할 정보
    class Meta:
        model = Character
        fields = ['user_id', 'name', 'attack', 'defense', 'hp', 'agility', 'intelligence']