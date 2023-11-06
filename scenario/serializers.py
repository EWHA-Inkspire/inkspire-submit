from .models import *
from rest_framework import serializers

# 스크립트 정보
class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ['background', 'genre', 'town', 'town_detail']