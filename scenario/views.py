from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# 스크립트 생성 뷰 (pk : character_id)
class ScriptView(views.APIView):
    serilalizer_class = ScriptSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        serializer = self.serilalizer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(character=character)
            return Response({
                'message' : '스크립트 생성 성공',
                'data' : serializer.data
            }, status=HTTP_200_OK)
        else:
            return Response({
                'message' : '스크립트 생성 실패',
                'data' : serializer.errors
            }, status=HTTP_400_BAD_REQUEST)

# 스크립트 상세 조회 뷰 (pk : script_id)
class ScriptListView(views.APIView):
    serilalizer_class = ScriptDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        data = get_object_or_404(Script, pk=pk)
        
        serializer = self.serilalizer_class(data)
        
        return Response({
            'message' : '스크립트 상세 조회 성공',
            'data' : serializer.data
        }, status=HTTP_200_OK)

# 목표 리스트 뷰 (pk : script_id)
class GoalListView(views.APIView):
    serilalizer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        script = get_object_or_404(Script, pk=pk)
        serializer = self.serilalizer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(script=script)
            return Response({
                'message' : '목표 생성 성공',
                'data' : serializer.data
            }, status=HTTP_200_OK)
        else:
            return Response({
                'message' : '목표 생성 실패',
                'data' : serializer.errors
            }, status=HTTP_400_BAD_REQUEST)

# 목표 상세 뷰 (pk : script_id, goal_pk : goal_id)
class GoalDetailView(views.APIView):
    serilalizer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        goal = get_object_or_404(Goal, pk=pk)
        self.check_object_permissions(self.request, goal.script)
        return goal
    
    def get(self, request, pk, goal_pk):
        goal = self.get_object(pk=goal_pk)
        
        serializer = self.serilalizer_class(goal)
        
        return Response({
            'message' : '목표 상세 조회 성공',
            'data' : serializer.data
        }, status=HTTP_200_OK)
    
    def patch(self, request, pk, goal_pk):
        goal = self.get_object(pk=goal_pk)
        serializer = self.serilalizer_class(data=request.data, instance=goal, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message' : '목표 정보 수정 성공',
                'data' : serializer.data
            }, status=HTTP_200_OK)
        else:
            return Response({
                'message' : '목표 정보 수정 실패',
                'data' : serializer.errors
            }, status=HTTP_400_BAD_REQUEST)

# GPT 대화내용 (pk : script_id)
class GptView(views.APIView):
    serilalizer_class = GptSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        script = get_object_or_404(Script, pk=pk)
        serializer = self.serilalizer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(script=script)
            return Response({
                'message' : 'GPT 쿼리 저장 성공',
                'data' : serializer.data
            }, status=HTTP_200_OK)
        else:
            return Response({
                'message' : 'GPT 쿼리 저장 실패',
                'data' : serializer.errors
            }, status=HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        gpts = Gpt.objects.filter(script=pk)
        serializer = self.serilalizer_class(gpts, many=True)
        
        return Response({
            'message' : 'GPT 조회 성공',
            'data' : serializer.data
        }, status=HTTP_200_OK)
    