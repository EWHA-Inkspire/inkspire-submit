from .models import *
from scenario.serializers import ScriptSerializer
from rest_framework import serializers

# 회원가입
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'nickname', 'password']
    
    # create 함수 overriding -> validated_data (유효성 검증 통과한 값) 기반 User 객체 생성
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            password = validated_data['password'],
            nickname = validated_data['nickname']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
# 로그인
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=128, write_only=True)
    
    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            
            if not user.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호입니다.')
            else:
                data = {
                    'nickname' : user.nickname,
                    'email' : user.email
                }
                
                return data
        else:
            raise serializers.ValidationError('이메일 주소를 다시 확인해주세요.')

# 캐릭터 정보
class CharacterSerializer(serializers.ModelSerializer):
    # 캐릭터가 지닌 스크립트 정보
    script = ScriptSerializer(many=False, read_only=True)
    class Meta:
        model = Character
        fields = ['name', 'script', 'attack', 'defense', 'hp', 'agility', 'intelligence']

# 프로필 정보
class ProfileSerializer(serializers.ModelSerializer):
    # user가 지닌 캐릭터 정보
    characters = CharacterSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['nickname', 'email', 'characters']
        read_only_fields = ('characters',)

