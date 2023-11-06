from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# 스크립트 생성 뷰
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
            