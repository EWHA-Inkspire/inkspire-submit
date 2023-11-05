from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    # 회원가입 & 로그인
    path('user/signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # 캐릭터 생성 / 조회
    path('character/get', views.CharacterList.as_view()),
    path('character/post', views.CharacterCreate.as_view()),
]
