from .models import User
from rest_framework import serializers

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