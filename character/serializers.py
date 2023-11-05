from .models import Character
from rest_framework import serializers

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