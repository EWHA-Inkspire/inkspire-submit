from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from .models import *
from .serializers import *

# 회원가입 뷰
class SignUpView(views.APIView):
    serializer_class = SignUpSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message' : '회원가입 성공',
                'data' : serializer.data
            }, status=HTTP_201_CREATED)
        return Response({
                'message' : '회원가입 실패',
                'data' : serializer.errors
        }, status=HTTP_400_BAD_REQUEST)

# 로그인 뷰
class LoginView(views.APIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            # 로그인이 성공한 경우, 토큰을 생성하고 사용자와 연결합니다.
            user = User.objects.get(email=serializer.validated_data['email'])
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message' : '로그인 성공',
                'data' : serializer.validated_data,
                'token': token.key # 토큰 값을 응답에 추가
            }, status=HTTP_200_OK)
        return Response({
            'message' : '로그인 실패',
            'data' : serializer.errors
        }, status=HTTP_400_BAD_REQUEST)

# 헤더에서 토큰 키 추출
def get_token_key(request):
    # 클라이언트의 인증 토큰을 추출
    authorization_header = request.META.get('HTTP_AUTHORIZATION')
    
    # 인증 토큰이 없을 경우 에러 처리
    if not authorization_header:
        raise AuthenticationFailed('인증 토큰이 필요합니다.')

    # "Token" 접두사를 제거하여 실제 토큰 값만 추출
    return authorization_header.split(" ")[1] if authorization_header else ''
    

# 특정 토큰 값을 사용하여 user_id 가져오기
def get_user_id_from_token(token_key):
    try:
        token = Token.objects.get(key=token_key)  # 토큰 조회
        user_id = token.user_id  # 토큰과 연결된 사용자의 user_id 가져오기
        return user_id
    except Token.DoesNotExist:
        return None  # 토큰이 없는 경우 처리

# 프로필 뷰
class ProfileView(views.APIView):
    serializer_class = ProfileSerializer

    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def get(self, request):
        auth_token = get_token_key(request=request)
        
        # token과 맵핑된 user_id 조회
        user_id = get_user_id_from_token(token_key=auth_token)
        data = get_object_or_404(User, pk=user_id)

        serializer = self.serializer_class(data)
        info = serializer.data

        return Response({
            'message': '프로필 조회 성공',
            'data': info
        }, status=HTTP_200_OK)

# 캐릭터 생성 뷰
class CharacterView(views.APIView):
    serilalizer_class = CharacterSerializer
    
    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def post(self, request):
        serializer = self.serilalizer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            auth_token = get_token_key(request=request)
            user_id = get_user_id_from_token(token_key=auth_token)
            
            user = get_object_or_404(User, pk=user_id)
            serializer.save(user=user)
            return Response({
                'message' : '캐릭터 생성 성공',
                'data' : serializer.data
            }, status=HTTP_200_OK)
        else:
            return Response({
                'message' : '캐릭터 생성 실패',
                'data' : serializer.errors
            }, status=HTTP_400_BAD_REQUEST)