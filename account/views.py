from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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
            return Response({
                'message' : '로그인 성공',
                'data' : serializer.validated_data
            }, status=HTTP_200_OK)
        return Response({
            'message' : '로그인 실패',
            'data' : serializer.errors
        }, status=HTTP_400_BAD_REQUEST)

# 프로필 뷰
class ProfileView(views.APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        data = get_object_or_404(User, pk=user.user_id)
        
        serializer = self.serializer_class(data)
        info = serializer.data
        
        return Response({
            'message' : '프로필 조회 성공',
            'data' : info
        }, status=HTTP_200_OK)

# 캐릭터 생성 뷰
class CharacterView(views.APIView):
    serilalizer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = self.serilalizer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({
                'message' : '캐릭터 생성 성공',
                'data' : serializer.data
            }, status=HTTP_200_OK)
        else:
            return Response({
                'message' : '캐릭터 생성 실패',
                'data' : serializer.errors
            }, status=HTTP_400_BAD_REQUEST)

# 캐릭터 조회 뷰 (user id로 조회)
class CharacterListView(views.APIView):
    serializer_class = CharacterSerializer
    
    def get(self, request, pk):
        serializer = self.serializer_class()