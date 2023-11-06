from .models import *
from rest_framework import serializers

# 스크립트 정보 - 캐릭터와 맵핑되는 정보 (목표, gpt 제외)
class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ['script_id', 'background', 'genre', 'town', 'town_detail']

# 목표 정보
class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['goal_id', 'content', 'final', 'finished']

# GPT 정보
class GptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gpt
        fields = ['gpt_id', 'role', 'query']

# 스크립트 세부 정보 - 스크립트 내용, 목표 + GPT 대화 내용도?
class ScriptDetailSerializer(serializers.ModelSerializer):
    # 스크립트가 지닌 목표 정보
    goals = GoalSerializer(many=True, read_only=True)
    
    class Meta:
        model = Script
        fields = ['background', 'genre', 'town', 'town_detail', 'goals']
