from django.urls import path, include
from .views import *

urlpatterns = [
    # 관리자 로그인
    path('api-auth/', include('rest_framework.urls')),
    # 회원가입, 로그인, 프로필 조회
    path('signup', SignUpView.as_view()),
    path('login', LoginView.as_view()),
    path('user/profile', ProfileView.as_view()),
    # 캐릭터 생성/조회
    path('character', CharacterView.as_view())
]
